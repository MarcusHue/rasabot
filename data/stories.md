

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

## click story

* greet
    - utter_greet
* ask_faq_the_dialog_manager
    - utter_faq_the_dialog_manager
* ask_faq_the_dialog_manager_location
    - utter_faq_the_dialog_manager_location
* ask_faq_the_dialog_manager_tech
    - utter_faq_the_dialog_manager_tech_stack_1
    - wait_one_second
    - utter_faq_the_dialog_manager_tech_stack_2

## Wromg language

* out_of_scope_non_english
    - utter_wrong_lang
* give_number
    - utter_goodbye

## start conversation

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

## New Story

* telljoke
    - action_tell_dad_joke

* tell_fav_breed
    -action_show_dog