import google.generativeai as genai
import random

def generateText(prompt, canGenerate):
    if prompt== "" or not canGenerate:
        return
    genai.configure(api_key="AIzaSyBSrR4G9tA5bYxL40xzT6TXAYQOdncr9hQ")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt).text
    return response

def generatePrimaryKey(length):
    preset = "abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    primaryKey = ""
    for x in range(length):
        primaryKey += preset[random.randint(0, len(preset)-1)]
    return primaryKey

