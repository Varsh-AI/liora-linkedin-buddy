# Liora 🤖 - LinkedIn Post Buddy

Liora is an AI-powered **LinkedIn Post Generator** that helps you create engaging posts in seconds!  
It supports multiple languages and post lengths, making it perfect for professionals who want to stay active on LinkedIn without spending hours writing content.

---

## **Features**

- Generate LinkedIn posts based on a **chosen topic**  
- Choose **post length**: Short, Medium, Long  
- Generate posts in **English or Hinglish**  
- User-friendly **Streamlit interface**  
- Supports AI models via **LangChain + Groq API**  

---

## **How it Works**

1. **Choose Topic:** Select the topic you want to write about.  
2. **Select Post Length:** Short, Medium, or Long.  
3. **Select Language:** English or Hinglish.  
4. **Generate Post:** Click the button to generate a LinkedIn post.  
5. **View Output:** Your AI-generated post appears below.  

### **Interface Screenshot**

![Liora LinkedIn Post Generator](Liora.png)

- **Title & tagline** show Liora branding.  
- **Dropdowns** let you pick topic, post length, and language.  
- **Generated post area** displays the AI output.  

---

## **Set-up**

1. **Get API Key**  
   - Go to: [https://console.groq.com/keys](https://console.groq.com/keys)  
   - Create an API key and update `.env` with your key:

2. **Install Dependencies**  

```bash
pip install -r requirements.txt
```  

3. **Run the Streamlit App**  

```bash
streamlit run main.py
```  
