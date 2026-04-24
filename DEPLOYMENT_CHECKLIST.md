# SmarterASP.NET Deployment Checklist

## 📋 Before Contacting Support

### ✅ Files Ready to Upload
- [ ] `app.py` - Main Flask application
- [ ] `wsgi.py` - WSGI entry point
- [ ] `requirements.txt` - Python dependencies
- [ ] `templates/index.html` - Frontend template

### ✅ Information You Need
- [ ] Your domain name: ___________________________
- [ ] Facebook App ID: 777094108561567
- [ ] Facebook App Secret: (keep secure)
- [ ] Verify Token: testtoken

---

## 📝 Prompt for SmarterASP Chatbot

**Copy the entire content from `SMARTERASP_CHATBOT_PROMPT.txt` and paste it into the SmarterASP chatbot.**

---

## 🎯 What to Expect from Support

They should tell you:

1. **Upload Location**
   - Example: `/httpdocs/` or `/wwwroot/` or `/public_html/`

2. **Python Setup Process**
   - Whether they configure it automatically
   - Or if you need to submit a ticket

3. **Package Installation**
   - How to install from requirements.txt
   - Whether they do it or you do it

4. **WSGI Configuration**
   - What WSGI server they use (gunicorn, uwsgi, etc.)
   - Configuration file needed

5. **Environment Variables**
   - Where to set them (control panel, .env file, etc.)

6. **Your Public URL**
   - What domain/URL your app will be accessible at

---

## 🚀 After Getting Instructions from Support

### Step 1: Upload Files
- Use FTP or File Manager
- Upload to the directory they specified
- Verify all files are uploaded

### Step 2: Python Environment Setup
- Follow their instructions for Python setup
- Wait for confirmation if they do it

### Step 3: Set Environment Variables
```
FB_APP_ID=777094108561567
FB_APP_SECRET=your_secret_here
VERIFY_TOKEN=testtoken
PORT=5000 (or whatever they specify)
```

### Step 4: Update Facebook Settings
1. Go to https://developers.facebook.com/
2. Select your app (ID: 777094108561567)
3. Go to WhatsApp → Configuration
4. Add to "Valid OAuth Redirect URIs":
   ```
   https://your-domain.com/callback
   ```
5. Save changes

### Step 5: Test Your App
1. Visit: https://your-domain.com
2. Check browser console (F12) for errors
3. Click "Connect WhatsApp" button
4. Complete OAuth flow
5. Verify it works!

---

## 🐛 Common Issues & Solutions

### Issue: "Module not found"
**Solution:** Ask support to install packages from requirements.txt

### Issue: "redirect_uri mismatch"
**Solution:** 
- Check Facebook settings
- Ensure URL matches exactly: `https://your-domain.com/callback`
- Check browser console for what URL is being used

### Issue: "500 Internal Server Error"
**Solution:**
- Check error logs in control panel
- Verify Python environment is configured
- Check if all files uploaded correctly

### Issue: "WebSocket connection failed"
**Solution:**
- Ask support if WebSockets are supported on Premium plan
- If not, you may need to remove flask-socketio

---

## 📞 Support Contact Methods

1. **Live Chat:** Use the chatbot with the prompt
2. **Support Ticket:** Control Panel → Support → Submit Ticket
3. **Email:** Check your welcome email for support email

---

## 🔐 Security Reminders

- [ ] Never commit `.env` file to git
- [ ] Keep FB_APP_SECRET secure
- [ ] Use HTTPS (should be default on SmarterASP)
- [ ] Don't share your FTP credentials

---

## ✅ Final Verification

After deployment, verify:
- [ ] App loads at your domain
- [ ] No console errors in browser (F12)
- [ ] "Connect WhatsApp" button appears
- [ ] Clicking button opens Facebook OAuth popup
- [ ] OAuth flow completes successfully
- [ ] Success message appears after connection

---

## 📝 Notes from Support

Write down what support tells you:

**Upload Directory:**
_____________________________________________

**Python Version:**
_____________________________________________

**WSGI Server:**
_____________________________________________

**Environment Variables Location:**
_____________________________________________

**Public URL:**
_____________________________________________

**Additional Steps:**
_____________________________________________
_____________________________________________
_____________________________________________
