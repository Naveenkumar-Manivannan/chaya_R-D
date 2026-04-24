# WhatsApp Embedded Signup - Flask App

A Flask application for WhatsApp Business API embedded signup flow.

## 🚀 Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Visit: `http://localhost:5000`

### Production Deployment (SmartASP)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## 📁 Project Structure

```
.
├── app.py                 # Main Flask application
├── wsgi.py               # WSGI entry point for production
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Frontend UI
├── .env.example         # Environment variables template
├── DEPLOYMENT.md        # Deployment guide
└── README.md           # This file
```

## ⚙️ Configuration

Copy `.env.example` to `.env` and update with your values:

```bash
FB_APP_ID=your_app_id
FB_APP_SECRET=your_app_secret
VERIFY_TOKEN=your_verify_token
PORT=5000
```

## 🔑 Facebook App Setup

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create or select your app
3. Add WhatsApp product
4. In **Settings → Basic**, note your App ID and App Secret
5. In **WhatsApp → Configuration**, add your redirect URI:
   - Format: `https://yourdomain.com/callback`

## 📝 Features

- ✅ WhatsApp Business embedded signup
- ✅ OAuth 2.0 authorization code flow
- ✅ Dynamic redirect URI (works with any domain)
- ✅ Production-ready
- ✅ Environment-based configuration

## 🛠️ Tech Stack

- **Backend**: Flask, Flask-SocketIO
- **Frontend**: Vanilla JavaScript, Facebook SDK
- **Deployment**: Gunicorn (WSGI server)

## 📖 How It Works

1. User clicks "Connect WhatsApp"
2. Facebook SDK opens OAuth popup
3. User completes WhatsApp Business setup
4. Facebook returns authorization code
5. Backend exchanges code for access token
6. Access token can be used to send WhatsApp messages

## 🐛 Troubleshooting

### "redirect_uri mismatch" error
- Ensure your domain is added to Facebook App settings
- Check that redirect URI matches exactly (including https://)

### App not loading
- Verify all environment variables are set
- Check server logs for errors
- Ensure dependencies are installed

## 📄 License

MIT
"# chaya_R-D" 
