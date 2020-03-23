## Long Conversation
* greet
  - utter_greet
* ask_mood
  - utter_akward
  - utter_no_feelings
* ask_faq_the_dialog_manager
  - utter_faq_the_dialog_manager
* ask_faq_chatbot_consultant
  - utter_faq_chatbot_consultant
* ask_faq_conversational_technology
  - utter_faq_conversational_technology
  - utter_initiate_number
* affirm
  - utter_ask_number
* give_number
  - utter_goodbye

## FAQ Chatbot
* ask_faq_chatbot
    - utter_faq_chatbot
* ask_more_information
    - utter_faq_chatbot_detail

## FAQ Dialog Manager
* ask_faq_the_dialog_manager
  - utter_faq_the_dialog_manager

## FAQ Chatbot Consultant
* ask_faq_chatbot_consultant
  - utter_faq_chatbot_consultant

## FAQ Conversational Technology
* ask_faq_conversational_technology
  - utter_faq_conversational_technology

## FAQ Intent
* ask_faq_intent
  - utter_faq_intent

## New Story

* greet
    - utter_greet
* ask_faq_the_dialog_manager
    - utter_faq_the_dialog_manager
* ask_faq_the_dialog_manager_location
    - utter_faq_the_dialog_manager_location
* ask_faq_the_dialog_manager_tech
    - utter_faq_the_dialog_manager_tech_stack_1
    - utter_faq_the_dialog_manager_tech_stack_2

## New Story

* out_of_scope_non_english
    - utter_wrong_lang
* give_number
    - utter_goodbye

## New Story

* start_conversation
    - utter_start_message

## New Story

* start_conversation
    - utter_start_message
* affirm
    - utter_bot_no_gender

## New Story

    - slot{"tech_stack":"rasa"}
* learn_more
    - utter_faq_the_dialog_manager_tech_stack_1
    - wait_0_second
    - utter_faq_the_dialog_manager_tech_stack_2
* learn_more{"tech_stack":"rasa"}
    - utter_faq_rasa_with_button
* learn_more{"tech_stack":"parloa"}
    - slot{"tech_stack":"parloa"}
    - utter_faq_parloa_without_button
    - utter_learn_more
* learn_more
    - utter_ask_number
* give_contacts
    - utter_confirm_contact
