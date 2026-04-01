=================================================================
MANU FORTI WEBSITE - DEPLOYMENT PACKAGE
=================================================================

This package contains everything you need to deploy manuforti.no

FILES INCLUDED:
- index.html (your website)
- README.txt (this file)
- DNS-SETTINGS.txt (Domeneshop DNS configuration)

=================================================================
STEP-BY-STEP DEPLOYMENT GUIDE
=================================================================

STEP 1: CREATE GITHUB ACCOUNT
-----------------------------
1. Go to https://github.com
2. Click "Sign up" (top right corner)
3. Enter your email address
4. Create a password
5. Choose a username (suggestion: jonathonmilne or manuforti)
6. Complete the signup process
7. VERIFY YOUR EMAIL (check your inbox for GitHub email)

STEP 2: CREATE REPOSITORY
-------------------------
1. Log in to GitHub
2. Click the green "New" button (or "+" icon → "New repository")
3. Repository name: manuforti-website
4. Description: Manu Forti Intelligence website
5. Select "Public" (must be public for free GitHub Pages)
6. CHECK the box "Add a README file"
7. Click "Create repository"

STEP 3: UPLOAD WEBSITE FILES
----------------------------
1. In your new repository, click "Add file" → "Upload files"
2. Drag and drop the index.html file from this package
3. Click "Commit changes"

STEP 4: ENABLE GITHUB PAGES
---------------------------
1. In your repository, click "Settings" (top menu)
2. Scroll down to "Pages" section (left sidebar)
3. Under "Source", select "Deploy from a branch"
4. Branch: select "main" and "/ (root)"
5. Click "Save"
6. Wait 2-5 minutes for the site to deploy
7. GitHub will show you the URL (https://yourusername.github.io/manuforti-website)

STEP 5: CONFIGURE DOMENESHOP DNS
--------------------------------
1. Log in to https://domeneshop.no
2. Click on "manuforti.no" in your domain list
3. Click "DNS" tab
4. Add the following DNS records (see DNS-SETTINGS.txt for details):
   - 4x A records pointing to GitHub IPs
   - 1x CNAME record for www
5. Save changes
6. Wait 15-60 minutes for DNS to propagate

STEP 6: VERIFY
--------------
1. Open browser
2. Go to https://manuforti.no
3. Your website should appear!

=================================================================
NEED HELP?
=================================================================
If you get stuck on any step, contact Aiden with:
- Which step you're on
- What error message you see (if any)

Good luck!
