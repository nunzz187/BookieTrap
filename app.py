{
  "component": "Bento",
  "props": {
    "use_case": "soccer-match",
    "cards": "lmss"
  },
  "children": [
    {
      "component": "SportScoreCard",
      "props": {
        "heading": "FIFA World Cup 2026™",
        "subheading": "Jun 27, 2026, 10:00 PM BST",
        "team_details": [
          {
            "component": "TeamDetail",
            "props": {
              "logo_image": {
                "component": "Image",
                "props": {
                  "src": "https://ssl.gstatic.com/onebox/media/sports/logos/optimized/9toerdOg8xW4CRhDaZxsyw_500x500.png"
                }
              },
              "name": "Croatia",
              "score": "",
              "is_winner": false
            }
          },
          {
            "component": "TeamDetail",
            "props": {
              "logo_image": {
                "component": "Image",
                "props": {
                  "src": "https://ssl.gstatic.com/onebox/media/sports/logos/optimized/VJQ1emg0TOubjGnap4vWuw_500x500.png"
                }
              },
              "name": "Ghana",
              "score": "",
              "is_winner": false
            }
          }
        ],
        "footer": "Lincoln Financial Field — Philadelphia",
        "corner_label": "Upcoming"
      },
      "actions": {
        "open_url": "https://www.foxsports.com/stories/soccer/2026-world-cup-croatia-ghana-odds-prediction-picks"
      }
    },
    {
      "component": "BentoCard",
      "props": {
        "size": "m",
        "heading": "4 Points",
        "subheading": "Guarantees Safety",
        "ext": {
          "status": "Clears 3rd-place cutoff"
        }
      },
      "actions": {
        "open_url": "https://www.theguardian.com/football/2026/jun/24/world-cup-groups-permutations-round-of-32-usa-mexico-canada"
      }
    },
    {
      "component": "BentoCard",
      "props": {
        "size": "s",
        "heading": "3 Pts",
        "subheading": "Senegal/S.Korea cap",
        "ext": {
          "cutoff": "Failed to reach 4"
        }
      },
      "actions": {
        "open_url": "https://www.theguardian.com/football/2026/jun/24/world-cup-groups-permutations-round-of-32-usa-mexico-canada"
      }
    },
    {
      "component": "BentoCard",
      "props": {
        "size": "s",
        "heading": "Under 2.5",
        "subheading": "Ghana Conceded",
        "ext": {
          "defense": "Clean sheets vs ENG/PAN"
        }
      },
      "actions": {
        "open_url": "https://www.livemint.com/sports/football-news/croatia-vs-ghana-when-where-to-watch-fifa-world-cup-match-globally-on-tv-online-win-prediction-lineups-more-11782552095628.html"
      }
    }
  ]
}
