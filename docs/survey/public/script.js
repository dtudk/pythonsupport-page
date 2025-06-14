// Configuration - use environment variables or config file
// Fixed API configuration
const API_BASE_URL = (() => {
  const currentOrigin = window.location.origin;
  const currentHost = window.location.hostname;
  
  // Check if we're in development (any localhost variant)
  const isDevelopment = currentHost === 'localhost' || 
                       currentHost === '::1' || 
                       currentHost === '127.0.0.1' ||
                       currentOrigin.includes('localhost') ||
                       currentOrigin.includes('[::1]');
  
  if (isDevelopment) {
    return 'http://localhost:80';
  }
  
  return ''; // Use same origin for production
})();

console.log('API_BASE_URL:', API_BASE_URL); // Debug log

// Robust CSV autocomplete loader (handles quoted line breaks and commas)
(async () => {
  try {
    const res = await fetch('./courses.csv');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const csv = await res.text();
    const lines = csv.split('\n');
    const records = [];
    let buffer = '';
    let inQuotes = false;
    lines.forEach(line => {
      const quoteCount = (line.match(/"/g) || []).length;
      if (!inQuotes) {
        buffer = line;
        if (quoteCount % 2 !== 0) {
          inQuotes = true;
        } else {
          records.push(buffer);
        }
      } else {
        buffer += '\n' + line;
        if (quoteCount % 2 !== 0) {
          inQuotes = false;
          records.push(buffer);
        }
      }
    });
    // drop header
    records.shift();
    const dl = document.getElementById('courses');
    records.forEach(record => {
      const idx = record.indexOf(',');
      const code = record.slice(0, idx).trim();
      let rawName = record.slice(idx + 1);
      rawName = rawName
        .replace(/\r/g, '')
        .replace(/CR$/, '')
        .replace(/^"+|"+$/g, '')
        .trim();
      const opt = document.createElement('option');
      opt.value = `${code} - ${rawName}`;
      dl.appendChild(opt);
    });
  } catch (err) {
    console.error('Error loading courses.csv:', err);
  }
})();

const buildingNumber = Number(new URLSearchParams(window.location.search).get('building')) || null;

const form = document.getElementById("surveyForm");
const modal = document.getElementById("thankYouModal");
const closeBtn = document.getElementById("closeModal");
const submitBtn = document.getElementById("submitBtn");
const errorDiv = document.getElementById("errorMessage");

function showError(message) {
  errorDiv.textContent = message;
  errorDiv.classList.remove('hidden');
}

function hideError() {
  errorDiv.classList.add('hidden');
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  hideError();
  
  // Disable submit button to prevent double submission
  submitBtn.disabled = true;
  submitBtn.textContent = 'Submitting...';
  
  try {
    const payload = {
      student_number: form.student_number.value.trim(),
      satisfaction: Number(
        form.querySelector('input[name="satisfaction"]:checked').value
      ),
      course_number: form.course_number.value.trim() || null,
      building_number: buildingNumber,
    };

    const response = await fetch(`${API_BASE_URL}/api/survey`, {
      method: "POST",
      headers: { 
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload)
    });

    const result = await response.json();

    if (!response.ok || !result.success) {
      throw new Error(result.errors?.join(', ') || result.message || 'Submission failed');
    }

    // Success - show modal and reset form
    modal.classList.remove('hidden');
    form.reset();
    
  } catch (error) {
    console.error("Survey submission error:", error);
    showError(error.message || 'Failed to submit survey. Please try again.');
  } finally {
    // Re-enable submit button
    submitBtn.disabled = false;
    submitBtn.textContent = 'Submit';
  }
});

closeBtn.addEventListener('click', () => {
  modal.classList.add('hidden');
});