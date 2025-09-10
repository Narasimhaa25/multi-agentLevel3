Multi-Agent Level 3

Level 3 — LLM + Multi-Step Tool Use (Full Agentic AI)

This project is the third level of a multi-stage AI assignment. At this level, we extend the LLM + single-tool chatbot from Level 2 into a multi-step agentic system.

The focus here is on multi-step reasoning and tool chaining:
	•	The agent breaks complex queries into multiple sub-tasks.
	•	Sub-tasks are delegated to the correct tool (calculator, translator) or directly answered by the LLM.
	•	Multiple steps can be executed in sequence (e.g., translate → calculate, or calculate → LLM).
	•	The chatbot maintains execution order and memory across steps.
	•	All interactions are logged with a timestamp for history.
⸻

⚙️ Setup and Installation
	1.	Ensure you have Python 3.9 or higher installed.

  	
   2.	Clone this repository and navigate to the level1 directory.
	
 3.	Install the required dependencies:
            pip install -r ../requirements.txt
            
   		 The requirements.txt file includes:
                    •	google-generativeai
                    •	python-dotenv
   4.	Create a .env file in the same directory with your Gemini API key:

     		GEMINI_API_KEY=your_api_key_here
5.	Run the chatbot:

  			 python chatbot_with_tool.py



💬 Example Interactions

   ✅ Example 1 Translate + Math
        You: `Translate 'Good Morning' into German and then multiply 5 and 6.
        Bot: 
            Guten Morgen
            Result: 30


 ✅ Example 2 — Translate + Math     

        You:  Add 10 and 20, then translate 'Have a nice day' into German
        Bot: 
             Result: 30
            Einen schönen Tag noch

✅ Example 3 — LLM + Tool:

         You: Tell me the capital of Italy, then multiply 12 and 12
         Bot: 
            Rome
            Result: 144
✅ Example 4 —Single-step: Translator only     
        	
		  You: Translate 'Sunshine' into Germa
         Bot:
               Sonnenschein

✅ Example 5—Multi-step: Multiple Calculations
	
 	You: Add 2 and 2 and multiply 3 and 3
	bot
 	Result: 4
	Result: 9
 ✅ Example 6—LLM only

		 		 What is the distance between Earth and Mars?
		Bot: The distance between Earth and Mars is constantly changing because both planets are orbiting the Sun at different speeds and distances.  There's no single answer.
		
		At their closest approach (a "close approach" or "opposition"), they can be roughly 54.6 million kilometers (33.9 million miles) apart.  At their furthest, they can be over 401 million kilometers (249 million miles) apart.

✅ Example 7—TESTING
					
	 You: WHAT IS MACHINE LEARNING
						
	  Bot: Machine learning (ML) is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.  Instead of being explicitly programmed, machine learning systems learn from data.  They identify patterns, make predictions, and improve their performance over time without being explicitly programmed for each specific task.
		
		Here's a breakdown of key aspects:
		
		* **Data:** ML algorithms rely heavily on data.  The more data, the better the algorithm can learn and make accurate predictions.  This data can be structured (like data in a spreadsheet) or unstructured (like images or text).
		
		* **Algorithms:** These are sets of rules and statistical techniques used to analyze data and identify patterns.  Different algorithms are suited for different types of problems and data.  Examples include linear regression, decision trees, support vector machines, and neural networks.
		
		* **Learning:**  The process of improving the algorithm's performance based on the data.  This can involve adjusting parameters within the algorithm to minimize errors or improve accuracy.  There are several types of learning:
		
		    * **Supervised learning:** The algorithm is trained on a labeled dataset (data where the desired output is known).  Examples include image classification (identifying cats vs. dogs) and spam detection.
		    * **Unsupervised learning:** The algorithm is trained on an unlabeled dataset (data where the desired output is not known).  Examples include clustering (grouping similar data points together) and dimensionality reduction.
		    * **Reinforcement learning:** The algorithm learns through trial and error by interacting with an environment and receiving rewards or penalties for its actions.  Examples include game playing (e.g., AlphaGo) and robotics.
		
		
		In essence, machine learning empowers computers to learn from experience without explicit programming, enabling them to perform tasks that would be difficult or impossible to program manually.  It's used in a wide range of applications, including image recognition, natural language processing, recommendation systems, fraud detection, and medical diagnosis.
		
		
<img width="1680" height="1050" alt="Screenshot 2025-09-10 at 19 22 08" src="https://github.com/user-attachments/assets/1a2c3058-09d4-476a-9025-50d9e74f9364" />

		 
		
