#!/usr/bin/env python3
"""
Simple HTTP Server for World Bank Data Visualizer
Serves the application locally for development and testing
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Configuration
PORT = 8000
HOST = "localhost"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler with CORS headers for API requests"""
    
    def end_headers(self):
        # Add CORS headers to allow API requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom log format"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def start_server():
    """Start the HTTP server"""
    try:
        # Change to the directory containing this script
        script_dir = Path(__file__).parent
        os.chdir(script_dir)
        
        # Create server
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            server_url = f"http://{HOST}:{PORT}"
            
            print("=" * 60)
            print("🌍 World Bank Data Visualizer - Development Server")
            print("=" * 60)
            print(f"📡 Server running at: {server_url}")
            print(f"📁 Serving files from: {script_dir}")
            print("🚀 Opening browser...")
            print("=" * 60)
            print("Press Ctrl+C to stop the server")
            print("=" * 60)
            
            # Open browser automatically
            try:
                webbrowser.open(server_url)
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print(f"Please manually navigate to: {server_url}")
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Try a different port or stop the existing server.")
            # Try alternative ports
            for alt_port in [8001, 8080, 3000, 5000]:
                try:
                    with socketserver.TCPServer((HOST, alt_port), CustomHTTPRequestHandler) as httpd:
                        server_url = f"http://{HOST}:{alt_port}"
                        print(f"✅ Using alternative port: {alt_port}")
                        print(f"📡 Server running at: {server_url}")
                        webbrowser.open(server_url)
                        httpd.serve_forever()
                except OSError:
                    continue
                break
            else:
                print("❌ No available ports found. Please check your system.")
        else:
            print(f"❌ Server error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    """Main function"""
    if len(sys.argv) > 1:
        try:
            global PORT
            PORT = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 8000.")
    
    # Check if index.html exists
    if not Path("index.html").exists():
        print("❌ index.html not found in current directory.")
        print("Please run this server from the project root directory.")
        sys.exit(1)
    
    start_server()

if __name__ == "__main__":
    main() 