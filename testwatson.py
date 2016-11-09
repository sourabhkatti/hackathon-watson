import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
from watson_developer_cloud import ConversationV1


def getchat():
    """
    The example returns a JSON response whose content is the same as that in
       ../resources/personality-v3-expect2.txt
    """

    texttosend = ''
    i = 0
    conversation = ConversationV1(
        username='6e28b0ef-6353-40f7-b13c-8881e7d134a3',
        password='fvU1aLdL7Ewf',
        version='2016-09-20')
    workspace_id = '204be5c7-0c5c-4239-a60d-29ac63cb979c'
    print("\n==================================\n")
    print("Welcome to PeerMind\n")

    print("\nHow are you?")

    contextprev = None


    while True:
        texttosend = input()
        if texttosend.find("quit") is not -1:
            print("\nIt was nice talking to you!\nHave a good day.")
            break
        # print(texttosend)
        response = conversation.message(workspace_id=workspace_id, message_input={'text': texttosend}, context=contextprev)
        contextprev = response['context']
        # print(json.dumps(contextprev, indent=2))

        try:
            print(response['output']['text'][0])
        except:
            print("We didn't understand your reply")


def getpersonality():
    ### PERSONALITY INSIGHTS
    #
    personality_insights = PersonalityInsightsV3(
        version='2016-10-20',
        username='6e28b0ef-6353-40f7-b13c-8881e7d134a3',
        password='fvU1aLdL7Ewf')
    with open(join(dirname(__file__),
                   'C:/Users/kattiso/IdeaProjects/hackathon-mh/resources/personality-v3.json')) as profile_json:
        profile = personality_insights.profile(
            profile_json.read(), content_type='application/json',
            raw_scores=True, consumption_preferences=True)

        print(json.dumps(profile, indent=2))

getchat()
