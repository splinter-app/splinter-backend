def generate_prompt(question: str, contexts: list):
  # character limit for the prompt
  limit = 3000


  # build our prompt with the retrieved contexts included
  prompt_start = (
      "Answer the question based on the context below.\n\n"+
      "Context:\n"
  )
  prompt_end = (
      f"\n\nQuestion: {question}\nAnswer:"
  )

  # Extract only the text from each context object
  context_texts = [context["text"] for context in contexts]

  # append contexts until hitting limit
  for i in range(1, len(context_texts)):
      if len("\n\n---\n\n".join(context_texts[:i])) >= limit:
          prompt = (
              prompt_start +
              "\n\n---\n\n".join(context_texts[:i-1]) +
              prompt_end
          )
          break
      elif i == len(context_texts)-1:
          prompt = (
              prompt_start +
              "\n\n---\n\n".join(context_texts) +
              prompt_end
          )
  return prompt


