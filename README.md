# 🧠 CodeSummarizer Mini

An AI-powered web application that lets you upload Python files and automatically generates concise, human-readable summaries for each function and class — making it useful for developers, code reviewers, and learners.

## 🚀 Live Demo
👉 [Click here to try it out](https://your-vercel-deployment-url.vercel.app) *(replace with actual URL)*

---

## 🛠️ Features

- 📄 Upload `.py` files directly in the browser
- 🤖 Automatically extracts functions and classes from the code
- 📝 Uses ML to generate meaningful summaries for each code block
- ⚡ Fast, intuitive, and responsive UI (built with React + TailwindCSS)
- 🧩 Handles small to moderately large codebases

---

## 💡 How It Works

1. **Upload File**: Users drag & drop or select a Python file.
2. **Code Parsing**: The backend extracts all function and class definitions using Python’s `ast` module.
3. **Text Summarization**: Summaries are generated using sentence-transformers and cosine similarity with a custom prompt-based approach.
4. **Display UI**: Each code block is shown alongside its AI-generated summary in a clean card layout.
