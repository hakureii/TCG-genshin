const { GoogleGenerativeAI } = require("@google/generative-ai");

const genAI = new GoogleGenerativeAI(process.env.API_KEY);

const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});

async function run() {
  const result = await model.generateContent(process.env.PROMPT);
  const response = await result.response;
  const text = response.text();
  console.log(text);
}

run();
