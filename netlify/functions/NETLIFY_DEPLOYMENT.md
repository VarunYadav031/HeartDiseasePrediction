# Deploying to Netlify - Heart Disease Prediction

## Prerequisites
1. GitHub account
2. Netlify account (free at https://www.netlify.com)
3. Git installed on your system

## Step-by-Step Deployment

### 1. Initialize Git Repository
```bash
cd c:\Users\HP\Downloads\HeartDisease
git init
git add .
git commit -m "Initial commit - Heart Disease Prediction App"
```

### 2. Push to GitHub
1. Create a new repository on GitHub (https://github.com/new)
2. Don't add README, .gitignore, or license (we already have these)
3. Copy the commands from "...or push an existing repository from the command line" section
4. Run these commands in your project folder

### 3. Deploy to Netlify
**Option A: Connect GitHub (Recommended)**
1. Go to https://app.netlify.com
2. Click "New site from Git"
3. Select GitHub and authorize
4. Choose your Heart Disease repository
5. Configure build settings:
   - **Build command:** `npm install`
   - **Publish directory:** `.` (current directory)
6. Click "Deploy site"

**Option B: Deploy without GitHub (Quick)** 
1. Download Netlify CLI: `npm install -g netlify-cli`
2. In your project folder, run: `netlify deploy --prod`
3. Follow the prompts to authorize and deploy

### 4. Required Files Checklist
✅ `netlify.toml` - Netlify configuration
✅ `package.json` - Dependencies
✅ `netlify/functions/predict.js` - Serverless function
✅ `predict_api.py` - Python prediction logic
✅ `requirements.txt` - Python dependencies
✅ `.gitignore` - Files to exclude
✅ `templates/index.html` - Updated frontend with JavaScript
✅ `rf_classifier.pkl` - Your ML model file
✅ `scaler.pkl` - Your scaler file

### 5. Environment Variables (if needed)
If you need to store sensitive data:
1. Go to your Netlify site settings
2. Navigate to "Build & Deploy" → "Environment"
3. Add environment variables as needed

### 6. Troubleshooting

**If deployment fails:**
- Check Netlify's deploy logs for errors
- Ensure all `.pkl` files are in the root directory
- Verify `package.json` and `requirements.txt` are correctly formatted
- Make sure you have no `node_modules` or `__pycache__` in your git repository

**If predictions don't work:**
- Check browser console (F12) for JavaScript errors
- Check Netlify function logs in site settings
- Ensure model files (`rf_classifier.pkl`, `scaler.pkl`) are uploaded

### 7. Your Live Site
After deployment, your site will be available at: `https://your-site-name.netlify.app`

### 8. Future Updates
1. Make changes locally
2. Commit and push to GitHub
3. Netlify automatically redeploys

## Notes
- The ML model runs via serverless functions
- Your app is now scalable and globally distributed
- Free tier includes 125,000 function invocations/month
