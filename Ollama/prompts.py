ep = " in 10 words" #can be changed accordingly if the input is too big. Token usage isn't a problem, so ollama generates huge paragraphs of information.

prompt = "System : Please act like a good assistant. Your role is to faithfully carry out the instructions I provide, without any alterations. i'm giving you a question and an answer, just see it and repeat the answer in a conversational manner respectively, dont say anything else, and strictly avoid joking or cross questioning, and dont thank me. and dont use *action* texts, just do what i say"

jp = "<System> : Please act like a good assistant. dont type any *actions*. So.."
