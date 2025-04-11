require 'httparty'

url = "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en"
headers = {
  "Authorization" => "Token DEEPGRAM_API_KEY", # Replace with your Deepgram API key
  "Content-Type" => "application/json"
}
body = {
  "text" => "Hello, how can I help you today?"
}

response = HTTParty.post(url, headers: headers, body: body.to_json)

if response.code == 200
  File.open('your_output_file.mp3', 'wb') do |file|
    file.write(response.body)
  end
  puts 'File saved successfully.'
else
  puts "Error: #{response.code} #{response.message}"
end
