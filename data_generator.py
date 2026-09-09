import json
import os
import config

def generate_mock_data():
    # Define all 25 Discourse topics (original 15 + 10 new deep research ones)
    topics = [
        # --- EVE Online (Originals) ---
        {
            "id": 101,
            "title": "How botting networks are actually stabilizing the mineral markets",
            "slug": "how-botting-networks-are-actually-stabilizing-the-mineral-markets",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "https://www.reddit.com/r/Eve/comments/1t5n1jh/this_is_not_ccp_chasing_a_trend_it_is_for_once/",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "MinerExtordinaire99",
                        "cooked": "<p>I have been analyzing the mineral markets in Jita for the past six months. The volume of Tritanium supplied by high-sec botting fleets is insane. These automated systems run 24/7 mine cycles. Without them, ship production costs would skyrocket, making capital ships unaffordable for smaller corporations. This is a weird symbiotic relationship. We hate the scripts and the RMT sellers (contact them at trite-supply@eve-rmt.net or check out http://eve-mineral-gold.com), but our economy depends on them. Is this a parasitism or is it a form of co-creation where bots build the foundation for human wars? Thoughts on this?</p>",
                        "created_at": "2026-06-25T10:15:30Z",
                        "like_count": 28,
                        "trust_level": 3,
                        "version": 2
                    }
                ]
            }
        },
        {
            "id": 102,
            "title": "Developer API for Market Bots - Yay or Nay?",
            "slug": "developer-api-for-market-bots-yay-or-nay",
            "jogo": "EVE Online",
            "fonte": "Fórum Oficial",
            "seccao": "Market Discussion",
            "url_fonte": "https://forums.eveonline.com/c/science-industry/market-discussion/",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "ESI_Coder_Omega",
                        "cooked": "<p>CCP provides the ESI API, which gives detailed market history. I written a Python script to automate my regional trading. The script checks price gaps, automatically computes margins, and alerts me on Discord when to update orders. I'm not using a clicker, just accessing data CCP allows. However, some players say that human traders can't compete with scripts running every 5 minutes. The developers are very transparent about the API access, but there's a risk of ruining the market for casual players. Let's discuss where we draw the line between fair automation and cheating.</p>",
                        "created_at": "2026-06-26T14:20:00Z",
                        "like_count": 14,
                        "trust_level": 4,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 103,
            "title": "Banwave statistics: Developer transparency is a joke!",
            "slug": "banwave-statistics-developer-transparency-is-a-joke",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "ShadowTrader_EVE",
                        "cooked": "<p>CCP just announced they banned 4,000 bot accounts this month. But they never release the methodologies. How do we know they aren't catching innocent players? The lack of transparency makes it impossible to assess the risk of running harmless trade helper scripts. I host a repository on github (https://github.com/helper-eve/trade-helper-bot) and users are scared. u/CCP_Swift, can we get clear guidelines? If the rules are opaque, players face high risk without knowing the boundaries.</p>",
                        "created_at": "2026-06-27T08:05:12Z",
                        "like_count": 55,
                        "trust_level": 2,
                        "version": 3
                    }
                ]
            }
        },
        {
            "id": 104,
            "title": "Automated defensive bubbles: Elite coding or exploit?",
            "slug": "automated-defensive-bubbles-elite-coding-or-exploit",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "FC_DoomSlayer",
                        "cooked": "<p>We fought a null-sec group last night that had instant defensive bubbles. As soon as our interceptor entered the grid, a script launched their bubble. There's no way a human reaction time is that fast (0.1 seconds consistently). They are co-creating a defense system entirely managed by AI monitors. It takes away the dialogue of tactical combat. The risk of losing expensive fleets to automated gate camps is driving people away from the game. Contact u/CCP_Support to investigate this player network.</p>",
                        "created_at": "2026-06-28T22:11:45Z",
                        "like_count": 42,
                        "trust_level": 3,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 105,
            "title": "Returning player looking for a high-sec industrial guild",
            "slug": "returning-player-looking-for-a-high-sec-industrial-guild",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "ChillMiner_Bob",
                        "cooked": "<p>Hey guys, I am returning to the game after a 4-year break. I have 20 million skill points, mostly in mining and refining. I want to find a friendly corp in high-sec. I'm not interested in null-sec wars or PvP, just chill mining and building ships. I have my own Orca. Hit me up if you are recruiting!</p>",
                        "created_at": "2026-06-27T16:45:00Z",
                        "like_count": 8,
                        "trust_level": 1,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 106,
            "title": "Jita is burning again",
            "slug": "jita-is-burning-again",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "JitaBurner",
                        "cooked": "<p>Title says it all. Massive lag and protests.</p>",
                        "created_at": "2026-06-28T18:22:00Z",
                        "like_count": 3,
                        "trust_level": 0,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 107,
            "title": "Neural networks in fleet operations: A test case",
            "slug": "neural-networks-in-fleet-operations-a-test-case",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "LogisticsGod_EVE",
                        "cooked": "<p>Our alliance ran a test using a machine learning model to optimize logistics ship allocation during battles. The model analyzed who was being targeted and directed shield repairs instantly. It felt like human-AI symbiosis, a very advanced dialogue. However, it violates EULA policies regarding external automated clients. The risk is high (permanent bans for directors), and we had to stop. CCP needs to allow this kind of technical co-creation. Read about our experiment here: http://nullsec-ml-logs.org.</p>",
                        "created_at": "2026-06-30T10:14:00Z",
                        "like_count": 19,
                        "trust_level": 3,
                        "version": 2
                    }
                ]
            }
        },

        # --- World of Warcraft (Originals) ---
        {
            "id": 201,
            "title": "The herb markets are ruined by automated druid trains",
            "slug": "the-herb-markets-are-ruined-by-automated-druid-trains",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "https://www.reddit.com/r/woweconomy/",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "GathererPro_WoW",
                        "cooked": "<p>Go to any zone in Khaz Algar and you will see 10 druids flying in a perfect line, gathering herbs simultaneously. They use software to mirror keypresses. This is parasitic value co-creation: they extract gold, sell it via RMT (Real Money Trading sites like http://wowgolddeals.org), and normal players get inflated consumable prices. Blizzard does nothing because these accounts pay subscription fees. The risk of market collapse is real. E-mail hacks and account theft are often linked to these operations. Avoid @GoldSeller_Rep.</p>",
                        "created_at": "2026-06-25T11:40:00Z",
                        "like_count": 87,
                        "trust_level": 2,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 202,
            "title": "Using Console Scripts for Rotation Automation",
            "slug": "using-console-scripts-for-rotation-automation",
            "jogo": "World of Warcraft",
            "fonte": "Fórum MMO-Champion",
            "seccao": "Interface & Addons",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "LuaKing_WoW",
                        "cooked": "<p>Is it bannable to use standard Lua console commands inside WoW to automate complex damage rotations? I wrote an addon that checks buff durations and flashes the next spell, but I want to take it further by having an external script read pixels to press keys. The game allows access to UI state, but pixel-reading scripts seem risky. Blizzard's warden anti-cheat is notoriously opaque about this. I want to discuss if rotation bots are co-creating a new form of high-end PvE or just destroying the game's core skills.</p>",
                        "created_at": "2026-06-26T19:00:15Z",
                        "like_count": 22,
                        "trust_level": 3,
                        "version": 4
                    }
                ]
            }
        },
        {
            "id": 203,
            "title": "AI-driven raid leaders: The future of guild coordination?",
            "slug": "ai-driven-raid-leaders-the-future-of-guild-coordination",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "MythicRaider_Pete",
                        "cooked": "<p>My guild has been testing an AI bot on Discord that integrates with our live combat logs. It analyzes our positioning and DPS output in real-time, giving voice callouts (e.g., 'Move left', 'Healer cooldown now'). It is a fascinating dialogue between human players and an AI coach. It increases our accessibility to mythic raiding by reducing human error, but it feels like we are losing the human connection. We are co-creating strategies with an AI agent. Is this cheating or just using technology?</p>",
                        "created_at": "2026-06-28T15:30:22Z",
                        "like_count": 134,
                        "trust_level": 4,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 204,
            "title": "RMT networks and their automated farming routes",
            "slug": "rmt-networks-and-their-automated-farming-routes",
            "jogo": "World of Warcraft",
            "fonte": "Fórum Oficial",
            "seccao": "Classic Discussion",
            "url_fonte": "https://www.reddit.com/r/wow/comments/1twvjwb/so_jagex_can_beat_bots_but_blizzard_cant/",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "ClassicPurist",
                        "cooked": "<p>RMT (Real Money Trading) is destroying the fabric of Classic WoW. Bot groups run dungeon scripts all night. They post their gold selling services on forums (visit http://classic-gold-quick.com or e-mail gold-support@wow-classic-rmt.com). They make the economy hyper-inflated. This is asymmetric and parasitic value creation. The risk of getting your account banned for buying from them is 90% now because Blizzard's new AI detection is active, but the sellers just generate new accounts. We need better developer transparency on how they trace gold flows.</p>",
                        "created_at": "2026-06-29T10:05:00Z",
                        "like_count": 52,
                        "trust_level": 2,
                        "version": 2
                    }
                ]
            }
        },
        {
            "id": 205,
            "title": "My fan art of Sylvanas Windrunner",
            "slug": "my-fan-art-of-sylvanas-windrunner",
            "jogo": "World of Warcraft",
            "fonte": "Fórum MMO-Champion",
            "seccao": "General Art",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "ElvenArtist",
                        "cooked": "<p>Check out this digital painting I finished yesterday! I spent about 12 hours on it. I wanted to capture Sylvanas's expression after the Shadowlands cinematic. You can see the full resolution version on my art station link. Let me know what you think of the lighting!</p>",
                        "created_at": "2026-06-28T09:12:00Z",
                        "like_count": 210,
                        "trust_level": 4,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 206,
            "title": "LF Group for Mythic+ Dungeon Run tonight",
            "slug": "lf-group-for-mythic-dungeon-run-tonight",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "MagePowa",
                        "cooked": "<p>Looking for a tank and a healer for a +10 Stonevault run tonight at 21:00 CET. We have three DPS (Mage, Rogue, Hunter) all around 2500 raider.io score. We want a smooth run, please know the tactics and have decent gear. Drop a comment with your character name and class!</p>",
                        "created_at": "2026-06-29T13:40:00Z",
                        "like_count": 6,
                        "trust_level": 1,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 207,
            "title": "WTS Gold cheap",
            "slug": "wts-gold-cheap",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "GoldSeller999",
                        "cooked": "<p>Email cheapwow@gold.com now!</p>",
                        "created_at": "2026-06-29T12:00:00Z",
                        "like_count": 0,
                        "trust_level": 0,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 208,
            "title": "AI gold farming scripts are getting smarter",
            "slug": "ai-gold-farming-scripts-are-getting-smarter",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "https://www.reddit.com/r/gamedev/",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "AntiBotCrusader",
                        "cooked": "<p>I saw a bot running in Bastion that didn't just farm; it actively fought back, dodged ground effects, and even waved at players to look human. The script makers are using behavior trees. They are co-creating a fake player base. If we try to speak to them, there is no dialogue. The transparency is zero since their code is closed. The risk is that Blizzard's server capacity is wasted on these scripts. Contact support at @Blizzard_CS to get this fixed.</p>",
                        "created_at": "2026-06-30T14:50:00Z",
                        "like_count": 45,
                        "trust_level": 2,
                        "version": 1
                    }
                ]
            }
        },

        # --- EVE Online (Deep Research Additions) ---
        {
            "id": 108,
            "title": "Market bots undercutting by 0.01 ISK in Jita",
            "slug": "market-bots-undercutting-by-0-01-isk-in-jita",
            "jogo": "EVE Online",
            "fonte": "Fórum Oficial",
            "seccao": "Market Discussion",
            "url_fonte": "https://forums.eveonline.com/c/science-industry/market-discussion/",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "Jita_Trader_Boss",
                        "cooked": "<p>Is it just me or are the market bots in Jita out of control again? I try to sell my faction modules and the exact same second I update my order, some character undercuts me by 0.01 ISK. I did this for an hour and the reaction time was always under 1 second. This is clearly an automated script using ESI or memory reading. It completely ruins the dialogue between buyers and sellers. The risk of trading is too high if you are not running a script. CCP needs to fix this because it's parasitic value extraction.</p>",
                        "created_at": "2026-06-30T15:20:10Z",
                        "like_count": 35,
                        "trust_level": 2,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 109,
            "title": "Ice mining bot fleets in High-sec",
            "slug": "ice-mining-bot-fleets-in-high-sec",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "IceColdTruth",
                        "cooked": "<p>We have a massive bot fleet in our high-sec system mining Ice 24/7. They have 10 Covetors and an Orca. As soon as a player enters the belt, they warp out to a safe spot. This automation is ruining the mineral economy by crashing the fuel block prices. However, some alliance leaders say it's good because it keeps the fuel block prices low for everyone. Is this a symbiotic co-creation or is it pure parasitism? We need transparency on how CCP tracks these fleets.</p>",
                        "created_at": "2026-06-30T18:45:00Z",
                        "like_count": 22,
                        "trust_level": 3,
                        "version": 2
                    }
                ]
            }
        },
        {
            "id": 110,
            "title": "CCP security team: Why we keep our detection methods secret",
            "slug": "ccp-security-team-why-we-keep-our-detection-methods-secret",
            "jogo": "EVE Online",
            "fonte": "Fórum Oficial",
            "seccao": "Announcements",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "CCP_Security_Official",
                        "cooked": "<p>CCP Games team explains why they cannot share the details of their anti-botting logs. If we release the exact metrics we use to identify botting networks, the script creators will immediately update their code to bypass our systems. This lack of transparency is necessary to protect the game's economy, although we understand it creates anxiety for players using third-party tools. We strive to maintain a dialogue, but security risk constraints must come first.</p>",
                        "created_at": "2026-06-30T09:00:00Z",
                        "like_count": 112,
                        "trust_level": 4,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 111,
            "title": "OCR tool for market scanning - safe to use?",
            "slug": "ocr-tool-for-market-scanning-safe-to-use",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "PythonOCR_Dev",
                        "cooked": "<p>I have written an OCR (Optical Character Recognition) tool that scans the game screen and exports market orders to a CSV. It doesn't inject any DLLs or read memory, it just takes screenshots. I think this is a fair tool for trade analysis, but some players say it violates the EULA because it automates data access. The developer guidelines are vague. What is the risk of getting banned for using OCR? We need more dialogue from CCP on this.</p>",
                        "created_at": "2026-07-01T02:15:30Z",
                        "like_count": 18,
                        "trust_level": 1,
                        "version": 3
                    }
                ]
            }
        },
        {
            "id": 112,
            "title": "Drake fitting for L3 missions",
            "slug": "drake-fitting-for-l3-missions",
            "jogo": "EVE Online",
            "fonte": "Reddit",
            "seccao": "r/Eve",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "NewbieDrake",
                        "cooked": "<p>Can anyone suggest a good Drake fit for running Level 3 security missions? I have T2 heavy missiles and passive shield tanks. I'm currently using a standard active build, but I struggle with cap stability. Thanks for any advice on rig selections and drone options!</p>",
                        "created_at": "2026-07-01T08:10:00Z",
                        "like_count": 5,
                        "trust_level": 2,
                        "version": 1
                    }
                ]
            }
        },

        # --- World of Warcraft (Deep Research Additions) ---
        {
            "id": 209,
            "title": "Cancel scanning on the Auction House is ruining the game",
            "slug": "cancel-scanning-on-the-auction-house-is-ruining-the-game",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/woweconomy",
            "url_fonte": "https://www.reddit.com/r/woweconomy/",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "CasualAHTrader",
                        "cooked": "<p>The auction house is unusable for casual players. People use addons like TSM (TradeSkillMaster) to cancel and relist hundreds of items every second. It's essentially automated cancel scanning. It mimics botting behavior. Legitimate players who just want to sell some herbs are locked out because their auctions are buried instantly. Blizzard's silence is deafening. This is a highly parasitic practice that destroys the market's accessibility.</p>",
                        "created_at": "2026-06-30T21:11:45Z",
                        "like_count": 98,
                        "trust_level": 3,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 210,
            "title": "Druid bot trains clipping through terrain in Khaz Algar",
            "slug": "druid-bot-trains-clipping-through-terrain-in-khaz-algar",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "AntiClipping_Squad",
                        "cooked": "<p>I just witnessed a train of 5 druids flying inside the mountains in Khaz Algar. They are clipping through the terrain to gather herbs from nodes that players can't reach. They must be using coordinate hacks and automated pathing. This is pure parasitism. If you whisper them, they don't reply, showing no human dialogue. The risk of game economy deflation is high. Please report them to @Blizzard_CS.</p>",
                        "created_at": "2026-06-30T23:05:00Z",
                        "like_count": 64,
                        "trust_level": 2,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 211,
            "title": "Warden bans Linux players using Wine - False Positives",
            "slug": "warden-bans-linux-players-using-wine-false-positives",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "LinuxWoWPlayer",
                        "cooked": "<p>Blizzard's Warden anti-cheat has started banning players running WoW on Linux via Wine. It seems Warden is flagging the translation layers as unauthorized third-party software. The lack of transparency on Warden's detection metrics is alarming. Innocent players are losing their accounts. We need an open dialogue with the development team. The risk of false positives is making people afraid to play on alternative operating systems.</p>",
                        "created_at": "2026-07-01T01:40:00Z",
                        "like_count": 145,
                        "trust_level": 4,
                        "version": 2
                    }
                ]
            }
        },
        {
            "id": 212,
            "title": "Automated RMT spam in Trade Chat",
            "slug": "automated-rmt-spam-in-trade-chat",
            "jogo": "World of Warcraft",
            "fonte": "Fórum Oficial",
            "seccao": "General Discussion",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "ChatSpamHater",
                        "cooked": "<p>Trade chat has become completely unreadable. Automated level 1 character scripts spam gold selling services and raid boosts every 3 seconds. They use scripts to bypass the chat throttling. Blizzard does nothing about this automated advertising. This is a parasitic practice that drives human players away. It destroys any potential for human dialogue in the trade channel. Visit http://cheap-gold-spam.com to see where they operate.</p>",
                        "created_at": "2026-07-01T04:50:00Z",
                        "like_count": 72,
                        "trust_level": 2,
                        "version": 1
                    }
                ]
            }
        },
        {
            "id": 213,
            "title": "ban the bots now!",
            "slug": "ban-the-bots-now",
            "jogo": "World of Warcraft",
            "fonte": "Reddit",
            "seccao": "r/wow",
            "url_fonte": "",
            "post_stream": {
                "posts": [
                    {
                        "id": 1,
                        "username": "SaltySpammer",
                        "cooked": "<p>Just ban them already.</p>",
                        "created_at": "2026-07-01T05:00:00Z",
                        "like_count": 1,
                        "trust_level": 1,
                        "version": 1
                    }
                ]
            }
        }
    ]

    # Clean existing data/raw folder first to avoid mixing old formats
    for f in os.listdir(config.DATA_RAW_DIR):
        if f.endswith(".json"):
            os.remove(os.path.join(config.DATA_RAW_DIR, f))

    # Write each topic into a separate topic_{id}.json file
    for topic in topics:
        file_name = f"topic_{topic['id']}.json"
        file_path = os.path.join(config.DATA_RAW_DIR, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(topic, f, indent=2, ensure_ascii=False)
        
    print(f"Discourse-native mock topics generated successfully in {config.DATA_RAW_DIR} ({len(topics)} files).")

if __name__ == "__main__":
    generate_mock_data()
