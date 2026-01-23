# Deploy to Render (Flask)

## Step 1: Prepare Your Repository
```bash
git add .
git commit -m "Add Render deployment config"
git push origin main
```

## Step 2: Deploy to Render

1. Go to https://render.com
2. Sign up with GitHub
3. Click **"New +"** → **"Web Service"**
4. Connect your GitHub repository: **HeartDiseasePrediction**
5. Fill in the configuration:
   - **Name:** heart-disease-prediction
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free tier (optional: choose Paid for persistence)

6. Click **"Create Web Service"**
7. Render will automatically deploy your app!

## Your App URL
After deployment, you'll get a URL like:
```
https://heart-disease-prediction.onrender.com
```

## Important Notes
- ✅ Your Flask app will be live
- ✅ ML models will work as before
- ⚠️ Free tier has limitations:
  - Instance spins down after 15 min of inactivity
  - Takes 30-50 sec to wake up
  - 0.5 GB RAM
- 💡 Upgrade to Paid ($7/month) for:
  - Always-on instances
  - Better performance
  - Persistent storage

## Troubleshooting

**If deployment fails:**
1. Check Render logs (Dashboard → Select Service → Logs)
2. Verify all model files are in repository:
   - `rf_classifier.pkl`
   - `scaler.pkl`
3. Make sure `requirements.txt` has all dependencies

**If predictions don't work:**
- Check that form data is being sent correctly
- Verify model files are accessible

## Alternative: Use Railway Instead

If you prefer Railway:
1. Go to https://railway.app
2. Click "Deploy from GitHub"
3. Select your repository
4. Railway auto-detects Python and deploys automatically
5. No additional config files needed!

Railway is slightly more generous ($5/month free credits).
