// var userLevel = userLevel || 'package-managed.html';

let userLevel;

function PyS_isOperatingSytem() {
    const userAgent = navigator.userAgent.toLowerCase();
    console.log('User Agent:', userAgent); // Debugging line
    if (userAgent.indexOf("android") != -1) return false;
    if (userAgent.indexOf("iphone") != -1) return false;
    if (userAgent.indexOf("ipad") != -1) return false;
    if (userAgent.indexOf("win") != -1) return "windows";
    if (userAgent.indexOf("mac") != -1) return "macos";
    if (userAgent.indexOf("linux") != -1) return "linux";
    return false;
}

function PyS_osSelector(os) {
    const baseUrl = getBaseUrl();
    console.log('Base URL:', baseUrl); // Debugging line
    if (os === "windows") {
        window.location.href = `${baseUrl}menu/${os}/fully-manual.html`;
    } else {
        window.location.href = `${baseUrl}menu/${os}/${userLevel}`;
    }
}

function PyS_redirectUser(UserLevel) {
    let os = PyS_isOperatingSytem();
    userLevel = UserLevel;
    console.log('Operating System:', os); // Debugging line
    const baseUrl = getBaseUrl();
    console.log('Base URL:', baseUrl); // Debugging line
    if (!os) {
        toggleBanner(); // Show os selector
    } else if (os === "windows") {
        window.location.href = `${baseUrl}menu/${os}/fully-manual.html`;
    } else {
        window.location.href = `${baseUrl}menu/${os}/${userLevel}`;
    }
}

function getBaseUrl() {
    // Get the path and remove the last segment
    let pathArray = window.location.pathname.split('/');
    pathArray.pop(); // Remove the last segment (current file name)
    
    // Join the remaining segments to form the new path
    let newPathname = pathArray.join('/');
    
    // Handle the case of local file URLs
    let origin = window.location.origin;
    if (origin === 'null') {
        origin = `file://${pathArray.slice(0, 2).join('/')}`; // Construct the file origin manually
        newPathname = '/' + pathArray.slice(2).join('/'); // Adjust the pathname accordingly
    }

    console.log('Constructed Path:', newPathname); // Debugging line
    return origin + newPathname + '/';
}

function toggleBanner() {
    const bannerContainer = document.getElementById('bannerContainer');
    const topBanner = document.querySelector('.topBanner');
    const bottomBanner = document.querySelector('.bottomBanner');
    const osSelector = document.getElementById('PyS_osSelector');

    if (bannerContainer && topBanner && bottomBanner && osSelector) {
        bannerContainer.classList.toggle('collapsed');
        // Delay the execution by 0.5 seconds (500 milliseconds)
        setTimeout(() => {
            topBanner.classList.toggle('hidden');
            bottomBanner.classList.toggle('hidden');
            osSelector.classList.toggle('hidden');
            bannerContainer.classList.toggle('collapsed');
        }, 500);
    } else {
        console.error('One or more elements not found');
    }
}

function noRed() {
    const bottomBanner = document.querySelector('.bottomBanner');
    if (bottomBanner) {
        bottomBanner.classList.toggle('hidden');
    } else {
        console.error('bottomBanner element not found');
    }
}
