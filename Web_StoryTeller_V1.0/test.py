from gradio_client import Client, handle_file

client = Client("emilalvaro/E2-F5-TTS")
result = client.predict(
		ref_audio_orig=handle_file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),
		ref_text="Hello!!",
		gen_text="Hello!!",
		exp_name="F5-TTS",
		remove_silence=False,
		cross_fade_duration=0.15,
		api_name="/infer"
)
print(result)