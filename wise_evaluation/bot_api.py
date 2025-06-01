#!/usr/bin/env python3
"""
FlyMy AI Bot API interface for image generation evaluation.
"""

import requests
import time
import os
from config import FLYMY_API_KEY, FLYMY_API_URL

class FlyMyAIBot:
    """Interface for FlyMy AI image generation API."""
    
    def __init__(self):
        """Initialize bot."""
        if not FLYMY_API_KEY:
            raise ValueError("FLYMY_API_KEY not found in environment")
        
        self.api_key = FLYMY_API_KEY
        self.api_url = FLYMY_API_URL
    
    def generate_image(self, prompt, output_path, max_retries=3):
        """Generate image from prompt and save to file."""
        try:
            # Generate image
            for attempt in range(max_retries):
                try:
                    success = self._make_api_request(prompt, output_path)
                    if success:
                        return True, prompt, prompt
                    
                    if attempt < max_retries - 1:
                        print(f"Retry {attempt + 1}/{max_retries}")
                        time.sleep(2)
                        
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_retries - 1:
                        time.sleep(2)
            
            return False, prompt, prompt
            
        except Exception as e:
            print(f"Image generation error: {e}")
            return False, prompt, prompt
    
    def _make_api_request(self, prompt, output_path):
        """Make API request to generate image."""
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Request body for image generation
        request_body = {
            "chat_history": [
                {
                    "role": "user",
                    "content": f"Generate image with prompt: {prompt}"
                }
            ]
        }
        
        try:
            # Start generation
            response = requests.post(self.api_url, headers=headers, json=request_body)
            
            if response.status_code != 200:
                print(f"API error {response.status_code}: {response.text}")
                return False
            
            request_id = response.json()['request_id']
            print(f"Generation started, request_id: {request_id}")
            
            # Poll for result
            api_url_result = f"https://api.chat.flymy.ai/chat-result/{request_id}"
            
            while True:
                try:
                    response_image = requests.get(api_url_result, headers=headers, timeout=10)
                    
                    if response_image.status_code != 200:
                        print(f"Error polling result: {response_image.status_code}")
                        return False
                    
                    result_data = response_image.json()
                    
                    if result_data.get('error') != 'Still processing':
                        # Generation completed
                        break
                    
                    print("Still processing...")
                    time.sleep(5)  # Wait 5 seconds before next check
                    
                except Exception as e:
                    print('Error in get image')
                    print(e)
                    return False
            
            # Download the image
            try:
                file_url = result_data['data']['file_url']
                full_url = f"https://api.chat.flymy.ai{file_url}"
                
                img_data = requests.get(full_url).content
                
                # Ensure directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                with open(output_path, 'wb') as handler:
                    handler.write(img_data)
                
                print(f"Image saved successfully: {output_path}")
                return True
                
            except Exception as e:
                print(result_data)
                print('Error in downloading image')
                print(e)
                return False
            
        except Exception as e:
            print(f"API request error: {e}")
            return False
    
    def wait_for_generation(self, max_wait_time=60):
        """Wait for image generation with progress indicator."""
        wait_time = 0
        while wait_time < max_wait_time:
            print(f"Waiting for image generation... ({wait_time + 1}/{max_wait_time})")
            time.sleep(1)
            wait_time += 1
        return True

# Legacy function for backward compatibility
def generate_image(prompt, output_path):
    """Legacy function - generates image"""
    bot = FlyMyAIBot()
    success, _, _ = bot.generate_image(prompt, output_path)
    return success

def test_api_connection():
    """Test if the API is working."""
    bot = FlyMyAIBot()
    
    test_prompt = "A simple red apple on a white background"
    test_output = "test_connection.png"
    
    print("Testing API connection...")
    success, _, _ = bot.generate_image(test_prompt, test_output)
    
    if success:
        print("✅ API connection successful!")
        if os.path.exists(test_output):
            os.remove(test_output)  # Clean up test file
        return True
    else:
        print("❌ API connection failed!")
        return False

if __name__ == "__main__":
    test_api_connection() 