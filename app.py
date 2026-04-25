from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO
import requests
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

# ========= CONFIG =========
# ⚠️ For production, use environment variables
APP_ID = os.getenv("FB_APP_ID", "777094108561567")
APP_SECRET = os.getenv("FB_APP_SECRET", "5267b614f80b74826749b9f9796bff2f")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "testtoken")

# Use Facebook's default redirect URI (always whitelisted)
REDIRECT_URI = "https://www.facebook.com/connect/login_success.html"

# ==========================

@app.after_request
def add_headers(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
    response.headers['Cross-Origin-Embedder-Policy'] = 'unsafe-none'
    return response


@app.route("/")
def index():
    # Use Facebook's default redirect URI (always whitelisted)
    redirect_uri = REDIRECT_URI
    
    print(f"🔍 INDEX - Redirect URI being sent to frontend: {redirect_uri}")
    
    return render_template("index.html", redirect_uri=redirect_uri)


# 🔥 TOKEN EXCHANGE (FIXED)
@app.route("/exchange-token", methods=["POST"])
def exchange_token():
    try:
        data = request.get_json()
        code = data.get("code")

        if not code:
            return jsonify({"success": False, "error": "No code provided"})

        # Use Facebook's default redirect URI (always whitelisted)
        redirect_uri = REDIRECT_URI
        
        print("\n📥 RECEIVED CODE:", code[:40] if len(code) > 40 else code)
        print("📥 USING REDIRECT URI:", redirect_uri)

        token_res = requests.get(
            "https://graph.facebook.com/v18.0/oauth/access_token",
            params={
                "client_id": APP_ID,
                "client_secret": APP_SECRET,
                "redirect_uri": redirect_uri,
                "code": code
            }
        ).json()

        print("📤 META RESPONSE:", token_res)

        if "access_token" not in token_res:
            return jsonify({"success": False, "error": token_res})

        return jsonify({
            "success": True,
            "access_token": token_res["access_token"]
        })

    except Exception as e:
        print("❌ ERROR:", str(e))
        return jsonify({"success": False, "error": str(e)})


@app.route('/callback')
def callback():
    return "✅ Callback received. You can close this window."


@app.route('/debug-config')
def debug_config():
    """Debug endpoint to check configuration"""
    return jsonify({
        "REDIRECT_URI": REDIRECT_URI,
        "APP_ID": APP_ID,
        "request_host": request.host,
        "request_scheme": request.scheme,
        "x_forwarded_proto": request.headers.get('X-Forwarded-Proto'),
        "x_forwarded_host": request.headers.get('X-Forwarded-Host')
    })


# ==========================
# 🚀 RUN APP
# ==========================
if __name__ == "__main__":
    # For local development
    port = int(os.getenv("PORT", 5000))
    
    print("\n🚀 APP RUNNING")
    print(f"🌍 PORT: {port}")
    print("📝 Redirect URI will be determined dynamically from incoming requests")
    
    socketio.run(app, host="0.0.0.0", port=port, debug=False)