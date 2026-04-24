# Deployment Guide for SmartASP

## 🚀 Changes Made

✅ **Removed ngrok** - No longer needed for production
✅ **Dynamic redirect URI** - Works with any domain automatically
✅ **Environment variables** - Secure configuration management
✅ **Production-ready** - Added gunicorn for WSGI server

---

## 📋 Pre-Deployment Checklist

### 1. Update Facebook App Settings

Go to your Facebook App Dashboard and add your SmartASP domain:

**In "Valid OAuth Redirect URIs":**
```
https://yourdomain.com/callback
```

Or if using a subdomain:
```
https://whatsapp.yourdomain.com/callback
```

### 2. Set Environment Variables

On SmartASP, set these environment variables:
- `FB_APP_ID` = Your Facebook App ID
- `FB_APP_SECRET` = Your Facebook App Secret
- `VERIFY_TOKEN` = Your webhook verify token
- `PORT` = 5000 (or whatever SmartASP requires)

---

## 🔧 Deployment Steps

### Option 1: Using Gunicorn (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Run with gunicorn
gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 wsgi:app
```

### Option 2: Direct Flask Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## 🌐 How It Works Now

The app **automatically detects** the domain from incoming requests:

- Local: `http://localhost:5000/callback`
- SmartASP: `https://yourdomain.com/callback`
- Custom domain: `https://whatever.com/callback`

**No hardcoded URLs!** Everything is dynamic.

---

## ✅ Testing After Deployment

1. Visit your deployed URL: `https://yourdomain.com`
2. Check browser console (F12) for: `🔍 REDIRECT_URI being used: https://...`
3. Click "Connect WhatsApp"
4. Complete the setup
5. Check server logs for: `📥 USING REDIRECT URI: https://...`

Both should show the **same URL** as what you added to Facebook settings.

---

## 🔒 Security Notes

- ✅ Never commit `.env` file to git
- ✅ Use environment variables for secrets
- ✅ Enable HTTPS on your domain
- ✅ Keep `FB_APP_SECRET` secure

---

## 🐛 Troubleshooting

### Error: "redirect_uri mismatch"
- Check Facebook App settings
- Ensure the URL in Facebook **exactly matches** your domain
- Check server logs to see what redirect_uri is being used

### Error: "Invalid config_id"
- Update the `config_id` in `templates/index.html` with your WhatsApp config ID

### App not loading
- Check if all dependencies are installed
- Verify environment variables are set
- Check server logs for errors

---

## 📞 Support

If you encounter issues, check:
1. Server logs for the redirect URI being used
2. Browser console for JavaScript errors
3. Facebook App Dashboard for configuration issues
