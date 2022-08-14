import threading,requests, random,os,time
        
guild_id = input("Guild ID ->")
channel_id = input("Channel ID ->")
message_id = input("Message ID ->")
r_r = input("Random report reason [Y/N]")
if not r_r:
    print("Reports reasopns -->\n[0] ILLEGAL CONTENT\n[1] HARASSMENT\n[2] SPAM OR PHISHING LINKS\n[3] SELF-HARM\n[4] NSFW CONTENT")
    c = input("->")
start = time.time()
r_count = 0

def Report(token, guild_id, channel_id, message_id, reason):
    global r_count
    Responses = {
            '401: Unauthorized': f'Invalid Discord token.',
            'Missing Access': f'Missing access to channel or guild.',
            'You need to verify your account in order to perform this action.': f'Unverified.'
    }

    json={
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason,
    }
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'sv-SE',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }

    report = requests.post('https://discordapp.com/api/v9/report', json=json, headers=headers)
    
    if (status := report.status_code) == 201:
        print(f"Report Successfully sent!\n")
        r_count +=1
        rps = r_count / int(start - time.time())
        os.system(f"title discord.gg/catcha Reports: {r_count} {int(rps)}/s - {abs(int(start - time.time()))}")
    elif status in (401, 403):
        print(Responses[report.json()['message']]+"\n")
    else:
        print(f"Error: {report.text} | Status Code: {status}\n")

for token in open('tokens.txt', "r"):   
    token = token.replace("\n","")  
    for x in range(200):  #0 ILLEGAL CONTENT #1 HARASSMENT #2 SPAM OR PHISHING LINKS #3 SELF-HARM #4 NSFW CONTENT
        if r_r:
            threading.Thread(target=Report, args=(token, guild_id, channel_id, message_id, random.randint(0,4),)).start()
        else:
            threading.Thread(target=Report, args=(token, guild_id, channel_id, message_id, c)).start()
