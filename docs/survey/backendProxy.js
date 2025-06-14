// server.js - Secure backend for survey submission\
require('dotenv').config();

const express = require('express');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');
const validator = require('validator');

const app = express();

// Security middleware
app.use(cors({
  origin: [
    'http://localhost:3000',
    'http://[::1]:3000',
    'http://127.0.0.1:3000',
    // Add any other origins you need
    ...(process.env.ALLOWED_ORIGINS ? process.env.ALLOWED_ORIGINS.split(',') : [])
  ],
  credentials: true,
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
app.use(helmet());
app.use(express.json({ limit: '10mb' }));

app.use(express.static('public'));

// Rate limiting
const surveyLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 submissions per IP per 15 minutes
  message: { error: 'Too many survey submissions. Please try again later.' }
});

// Environment variables (store these securely)
const AZURE_ENDPOINT = process.env.AZURE_LOGIC_APP_ENDPOINT;

// Validation schema
function validateSurveyData(data) {
  const errors = [];
  
  // Validate student number
  if (!data.student_number || !/^\d{6}$/.test(data.student_number)) {
    errors.push('Student number must be exactly 6 digits');
  }
  
  // Validate satisfaction rating
  if (!data.satisfaction || !Number.isInteger(data.satisfaction) || 
      data.satisfaction < 1 || data.satisfaction > 5) {
    errors.push('Satisfaction must be an integer between 1 and 5');
  }
  
  // Validate course number (optional)
  if (data.course_number && typeof data.course_number !== 'string') {
    errors.push('Course number must be a string');
  }
  
  // Sanitize course number
  if (data.course_number) {
    data.course_number = validator.escape(data.course_number.trim());
    if (data.course_number.length > 200) {
      errors.push('Course number too long');
    }
  }

  // Sanitize building number
  if (!data.building_number || !Number.isInteger(data.building_number) || 
      data.building_number < 100 || data.building_number > 500) { 
        errors.push('Building number must be between 100 and 500');
    }

  
  return { isValid: errors.length === 0, errors, sanitizedData: data };
}

// Survey submission endpoint
app.post('/api/survey', surveyLimiter, async (req, res) => {
  try {
    // Validate request data
    const validation = validateSurveyData(req.body);
    
    if (!validation.isValid) {
      return res.status(400).json({
        success: false,
        errors: validation.errors
      });
    }
    
    // Prepare payload for Azure Logic App
    const payload = {
      student_number: "s" + validation.sanitizedData.student_number,
      satisfaction: validation.sanitizedData.satisfaction,
      course_number: validation.sanitizedData.course_number || null,
      building_number: validation.sanitizedData.building_number || null
    };
    
    // Submit to Azure Logic App
    const response = await fetch(AZURE_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        //...(API_KEY && { 'Authorization': `Bearer ${API_KEY}` })
      },
      body: JSON.stringify(payload)
    });
    
    if (!response.ok) {
      console.error('Azure Logic App error:', response.status, await response.text());
      return res.status(500).json({
        success: false,
        message: 'Failed to submit survey'
      });
    }
    
    // Success response (don't expose internal details)
    res.json({
      success: true,
      message: 'Survey submitted successfully'
    });
    
  } catch (error) {
    console.error('Survey submission error:', error);
    res.status(500).json({
      success: false,
      message: 'Internal server error'
    });
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});


const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Survey API server running on port ${PORT}`);
});

module.exports = app;