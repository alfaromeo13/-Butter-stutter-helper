import requests
import constants
import json
from auth import OPENAI_KEY

import openai
openai.api_key = OPENAI_KEY


def get_text(audio_file: bytes) -> str:
    files = [
        ('audio_file', ('filename', audio_file, 'audio/mpeg'))
    ]
    response = requests.request("POST", constants.URL, data={}, files=files)
    return json.loads(response.text)['text']


def get_answer(q: str) -> str:
    instruction: str = 'I am an intelligent question-answering bot that helps people who stutter.' \
                       ' If you ask me a question about stuttering, I will answer.' \
                       ' If you ask me a question that is nonsense, trickery, or irrelevant for stuttering,' \
                       ' I will respond with: "Please ask me about stuttering."'
    prompt: str = f'{instruction}' \
                  f'\n' \
                  f'\n{qna_bank}' \
                  f'\nQ: {q}' \
                  f'\nA: '
    completion = openai.Completion.create(
        model='text-davinci-002',
        prompt=prompt,
        temperature=0,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return completion.choices[0].text


qna_bank: str = """Q: If a person has stuttering problems, should I finish their sentence?
A: Stuttering is different from a word-finding disfluency in which you get stuck in a sentence because you can’t find the word you want to use. This is referred to as a language block; stuttering is a speech block. During a moment in which you just can’t think of a certain word, it can be helpful to have someone finish your sentence. However, a person who stutters knows exactly which word they want to say, but it is physically stuck. If you are unsure of how to react when a person who stutters is in a block, just ask.

Q: Should I hold eye contact when people are stuttering?
A: It is polite to maintain eye contact when speaking with someone, and there should be no exception for someone who stutters. You may feel like you should break eye contact to prevent a person who stutters from feeling uncomfortable, but it may actually give off the idea that you are uncomfortable.

Q: If many children outgrow their stutter, can an adult outgrow theirs?
A: It is unlikely that an adult will outgrow their stutter. Recovery rates are high in early childhood but decrease steadily with age. However, this does not mean that they can not overcome it. A person can overcome their stuttering by no longer avoiding certain words, saying everything they want to say, and participating in society without allowing their stutter to hold them back.

Q: Is it normal for a person who stutters to stutter more when they are tired?
A: Being tired, sick, stressed, etc can be a trigger for stuttering, but it is not a cause. Triggers can include anything from anxiety to sleep deprivation.

Q: What is stuttering?
A: Stuttering is a speaking and communication disorder. It's a certain automated speaking pattern and a certain state associated with it. We usually neglect the emotional part of stuttering. Yet, the invisible part of stuttering is huge. That's the real reason why we want to do something about stuttering or about our attitude to stuttering.

Q: What causes stuttering?
A: Genetics, heredity, neurology, traumas, repression of emotions - all can contribute to the development of stuttering.  Yet, once stuttering is formed it becomes an automated muscle and emotional memory. It starts to reproduce itself. From this perspective, we can say that stuttering becomes the main cause of stuttering in and of itself.

Q: Is there any medicine or device that can cure stuttering?
A: No. Medications tend to try to relax our bodies. Devices and apps tend to try to correct our speaking while we use them. They don't promise to change our speaking pattern. Actually, nothing can "cure" stuttering. Stuttering treatment mindset, when we expect somebody to do something magical to us or to teach us some magic trick, doesn't get us far. Instead, it gets us further away from real change.

Q: How common is having stuttering problems?
A: About 8% of children stutter, according to the Action for Stammering Children NGO.

Q: How to stop stuttering?
A: Stuttering is an automated speaking pattern. "Automated" by definition means that there's no way to just "stop" stuttering. However, by creating new automated muscle and emotional memory we remove the anticipation, anxiety, and tension associated with speaking.

Q: Why I don't stutter alone?
A: That's a very common question. Many people who stutter don't stutter alone or at least stutter much less speak to themselves. Speaking is interaction. It's not only articulating sounds. The invisible part of stuttering becomes visible when we speak in front of new people. An oral answer at school, exam, job interview, or even being around friends when we want to be our best.

Q: Why I don't stutter when I sing?
A: Stuttering is a certain structure of speaking. Or to be more precise, the lack of structure. We don't quite feel the structure. Speaking seems to be an endless effort to get through the speech impediments. Breaks in breathing and voicing, no pauses, hard sounds, and tension both physical and emotional. The rhythmical structure is impaired. So, we want to bring some elements from singing to our speaking - more substance, rhythm, stresses, and music.

Q: Why do I stutter on certain "hard" sounds and words?
A: Even though we often have our "favorite" sounds and words they just represent stuttering. Any sound can become "hard" especially when we can't replace it (like in the name, address, etc.) I suggest playing with the hard sounds and words in two ways. First, detach the "hard" sound when it's the first sound. Like playing with "esent - present," "ositive-positive." Trying to feel that we want to say the vowel sound rather than the consonant. And second, we want to feel the connection between the words, we want to feel one airflow in the speaking piece, like in "when we stop speaking" we don't want to stop the airflow after "stop," we want to say "sto-psreaking" getting from "o" straight to "i:" in "speaking."

Q: How to deal with stuttering anxiety?
A: There are great tips - to breathe, to make pauses, to change our mindset and concentrate on the message, to open up about stuttering, etc. But we want to be clear that stuttering anxiety and tension actually represent stuttering. If there's no anxiety and tension, physical and emotional tension, attached to the speech impediments then there's no stuttering. So, again we want to consider the path of building a training speech and a new speaking pattern rather than fighting the anxiety. We don't want to give ground for that anxiety and tension in the first place.

Q: Speech therapy or self-help?
A: I'm a big fan of both. Reading out loud, talking to the mirror or the exercises that I suggest doing below. Yet, we want to realize that speaking is interaction. So, we want to move from speaking to ourselves to speaking to other people. And speech therapy (good speech therapy) does exactly that - gets us to speak to other people. And makes that process step-by-step where we attach confidence to the very act of speaking step-by-step.

Q: What stuttering techniques would you recommend?
A: The main idea about the techniques is that when we apply the techniques to our current speaking pattern, in fact, we're just trying to escape stuttering, we're running away from it. Instead of avoiding stuttering, I would suggest thinking about creating a new speaking pattern. Feeling the security and confidence in the technique that you use. And of course - enjoy it!

Q: What speaking exercises for stuttering would you recommend?
A: Yes, we do want to play with our breathing, voicing, articulation, engaging our body and eye-contact, but at the same time, we don't want to stay with ourselves when doing those exercises. We want to move that great feeling to interaction.

Q: Can I live a happy life with stuttering?
A: We definitely want to get more positive about ourselves (and about stuttering because it's part of us right now)! We want to focus on the things that we love doing. We don't want to hide stuttering. Because as we hide stuttering we hide ourselves. We have something to share. We have a message. This way we create space in our life that doesn't belong to stuttering. We become open, active, and positive about speaking interaction. That's the best start to overcoming stuttering and getting free from stuttering."""
