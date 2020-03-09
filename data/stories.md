## happy path
* greet
  - utter_greet
* mood_great
  - action_tell_chuck_norris_joke

## first trial
* greet
  - utter_greet
* ask_mood
  - utter_akward
  - utter_no_feelings
* ask_faq
  - respond_faq
* ask_faq
  - respond_faq
* ask_faq
  - respond_faq
  - utter_initiate_number
* affirm
  - utter_ask_number
* give_number
  - utter_goodbye
