if __name__ == "__main__":
	try:
		__import__("enc_20").security()
	except Exception as e:
		exit(str(e))
