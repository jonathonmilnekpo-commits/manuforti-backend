#!/usr/bin/env python3
"""
Crab Content Generator Tool
Automates creation of social media content for OpenClawExpert
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

class CrabContentGenerator:
    def __init__(self):
        self.templates = {
            'x': {
                'quick_tip': [
                    "💡 OpenClaw Tip:\n\n{tip}\n\n{hashtags}",
                    "🦀 Did you know?\n\n{tip}\n\nSave this for later!",
                    "Quick win with OpenClaw:\n\n{tip}\n\nTakes 2 minutes to set up.",
                ],
                'before_after': [
                    "Before OpenClaw:\n❌ {before}\n\nAfter OpenClaw:\n✅ {after}\n\nTime saved: {time_saved}\n\n{hashtags}",
                    "I used to spend {time_before} on {task}.\n\nNow OpenClaw does it in {time_after}.\n\nHere's how 👇",
                ],
                'question_poll': [
                    "Quick poll:\n\nWhat's your biggest time waster?\n\nA) {option_a}\nB) {option_b}\nC) {option_c}\nD) Other (reply)\n\nI'll share how OpenClaw can automate the winner tomorrow.",
                    "Be honest:\n\n{question}\n\nReply with your answer 👇",
                ],
                'proof': [
                    "Here's what OpenClaw automated for me this {time_period}:\n\n{automation_list}\n\nTotal time saved: {time_saved}",
                    "OpenClaw just {action} while I {doing_what}.\n\nI didn't touch a thing.\n\nThis is what {time_period} looks like now.",
                ],
                'thread_hook': [
                    "I automated my entire {workflow} with OpenClaw.\n\nHere's the exact setup (thread): 🧵",
                    "OpenClaw saved me {time_saved} this week.\n\nHere's how I did it:\n\n🧵",
                    "Most people don't know this OpenClaw trick:\n\n🧵",
                ],
            },
            'instagram': {
                'reel': [
                    "{hook}\n\n{tip}\n\nFollow @openclawexpert for daily automation tips! 🦀\n\n{hashtags}",
                    "{hook}\n\n{before_after}\n\nSave this! 💾\n\n{hashtags}",
                ],
                'carousel': [
                    "{title}\n\nSwipe to see {swipe_content} →\n\n{hashtags}",
                ],
            },
            'youtube': {
                'title': [
                    "I Automated My {task} with OpenClaw (Saved {time_saved})",
                    "OpenClaw vs {alternative}: Which is Better?",
                    "How I Save {time_saved} Every Week with OpenClaw",
                    "OpenClaw Tutorial: {topic} for Beginners",
                    "I Built a {automation_type} in 10 Minutes with OpenClaw",
                ],
                'description': [
                    """🦀 {hook}

In this video, I show you {what_you_show}.

⏱️ TIMESTAMPS:
0:00 - {timestamp_1}
{timestamp_2}
{timestamp_3}
{timestamp_4}
{timestamp_5}

🔗 LINKS:
OpenClaw: https://openclaw.ai
Setup Services: [link]

📧 NEWSLETTER:
Get weekly OpenClaw tips: [link]

#openclaw #ai #automation #productivity""",
                ],
            }
        }
        
        self.content_pillars = [
            'morning_routine',
            'email_automation',
            'calendar_management',
            'research_automation',
            'content_creation',
            'social_media',
            'data_analysis',
            'security_best_practices',
            'skill_reviews',
            'client_case_studies',
        ]
        
        self.hashtag_pools = {
            'general': ['#OpenClaw', '#AIAutomation', '#Productivity', '#AITools'],
            'advanced': ['#OpenClawExpert', '#AIAgents', '#WorkflowAutomation', '#BuildInPublic'],
            'beginner': ['#OpenClawTips', '#GettingStarted', '#AITutorial', '#TechTips'],
        }
    
    def generate_x_post(self, post_type='quick_tip', **kwargs):
        """Generate an X post"""
        template = random.choice(self.templates['x'][post_type])
        
        # Default values
        defaults = {
            'tip': self._get_random_tip(),
            'hashtags': ' '.join(random.sample(self.hashtag_pools['general'], 3)),
            'before': 'Manually sorting emails for 30 minutes',
            'after': 'OpenClaw sorts them automatically',
            'time_saved': '5 hours/week',
            'time_before': '2 hours',
            'time_after': '5 minutes',
            'task': 'email management',
            'option_a': 'Email',
            'option_b': 'Meetings',
            'option_c': 'Data entry',
            'question': 'How many hours do you waste on repetitive tasks each week?',
            'time_period': 'morning',
            'automation_list': '✅ Checked calendar\n✅ Sorted emails\n✅ Updated tasks',
            'action': 'sent my daily briefing',
            'doing_what': 'was sleeping',
            'workflow': 'morning routine',
        }
        defaults.update(kwargs)
        
        return template.format(**defaults)
    
    def generate_instagram_caption(self, post_type='reel', **kwargs):
        """Generate an Instagram caption"""
        template = random.choice(self.templates['instagram'][post_type])
        
        defaults = {
            'hook': self._get_random_hook(),
            'tip': self._get_random_tip(),
            'before_after': 'Before: 2 hours of manual work\nAfter: 5 minutes of setup',
            'hashtags': ' '.join(random.sample(self.hashtag_pools['general'] + self.hashtag_pools['advanced'], 5)),
            'title': '5 OpenClaw Automations You Need',
            'swipe_content': 'the 5 automations',
        }
        defaults.update(kwargs)
        
        return template.format(**defaults)
    
    def generate_youtube_title(self, **kwargs):
        """Generate a YouTube video title"""
        template = random.choice(self.templates['youtube']['title'])
        
        defaults = {
            'task': 'Morning Routine',
            'time_saved': '10 Hours',
            'alternative': 'ChatGPT',
            'topic': 'Email Automation',
            'automation_type': 'Lead Qualification System',
        }
        defaults.update(kwargs)
        
        return template.format(**defaults)
    
    def generate_youtube_description(self, **kwargs):
        """Generate a YouTube video description"""
        template = self.templates['youtube']['description'][0]
        
        defaults = {
            'hook': "In this video, I show you how to automate your entire morning routine with OpenClaw.",
            'what_you_show': 'the exact setup that saves me 45 minutes every day',
            'timestamp_1': 'The problem with manual mornings',
            'timestamp_2': '1:30 - My old routine',
            'timestamp_3': '3:00 - The OpenClaw solution',
            'timestamp_4': '5:00 - Step-by-step setup',
            'timestamp_5': '8:00 - Results & next steps',
        }
        defaults.update(kwargs)
        
        return template.format(**defaults)
    
    def generate_week_content(self, week_number=1):
        """Generate a full week of content"""
        week_plan = {
            'week': week_number,
            'dates': (datetime.now() + timedelta(weeks=week_number-1)).strftime('%Y-%m-%d'),
            'x_posts': [],
            'instagram_posts': [],
            'youtube_videos': [],
        }
        
        # Generate 21 X posts (3/day)
        for day in range(7):
            for _ in range(3):
                post_type = random.choice(['quick_tip', 'before_after', 'question_poll', 'proof'])
                week_plan['x_posts'].append({
                    'day': day + 1,
                    'type': post_type,
                    'content': self.generate_x_post(post_type),
                })
        
        # Generate 7 Instagram posts (1/day)
        for day in range(7):
            week_plan['instagram_posts'].append({
                'day': day + 1,
                'type': 'reel',
                'caption': self.generate_instagram_caption(),
            })
        
        # Generate 2-3 YouTube videos
        for _ in range(random.randint(2, 3)):
            week_plan['youtube_videos'].append({
                'title': self.generate_youtube_title(),
                'description': self.generate_youtube_description(),
            })
        
        return week_plan
    
    def _get_random_tip(self):
        """Get a random OpenClaw tip"""
        tips = [
            "Use the Email Sorter skill to automatically categorize your inbox.",
            "Set up a morning briefing that checks calendar, weather, and news.",
            "Create a skill that prepopulates meeting notes from calendar invites.",
            "Use OpenClaw to monitor competitor websites for changes.",
            "Automate your daily standup report with data from multiple sources.",
            "Set up OpenClaw to track your portfolio and alert on price changes.",
            "Create a skill that summarizes long articles in 3 bullet points.",
            "Use OpenClaw to automatically generate weekly reports.",
            "Set up reminders that include context from previous conversations.",
            "Create a skill that books meetings based on your availability.",
        ]
        return random.choice(tips)
    
    def _get_random_hook(self):
        """Get a random video hook"""
        hooks = [
            "This OpenClaw automation saved me 10 hours this week.",
            "I haven't checked my email in 3 days. Here's why:",
            "My calendar organizes itself now.",
            "OpenClaw does my morning routine while I sleep.",
            "I automated my entire job search with OpenClaw.",
        ]
        return random.choice(hooks)
    
    def save_content_plan(self, content_plan, filename=None):
        """Save content plan to file"""
        if filename is None:
            filename = f"content_plan_week_{content_plan['week']}.json"
        
        output_path = Path.home() / ".openclaw" / "workspace" / "crab" / "generated_content" / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(content_plan, f, indent=2)
        
        print(f"✓ Content plan saved to: {output_path}")
        return output_path
    
    def generate_text_output(self, content_plan):
        """Generate human-readable text output"""
        output = []
        output.append(f"# Content Plan — Week {content_plan['week']}\n")
        output.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        output.append("## X Posts (21 total)\n\n")
        for i, post in enumerate(content_plan['x_posts'], 1):
            output.append(f"### Post {i} (Day {post['day']}) — {post['type']}\n")
            output.append(f"{post['content']}\n\n")
            output.append("---\n\n")
        
        output.append("## Instagram Posts (7 total)\n\n")
        for i, post in enumerate(content_plan['instagram_posts'], 1):
            output.append(f"### Day {post['day']}\n")
            output.append(f"{post['caption']}\n\n")
            output.append("---\n\n")
        
        output.append("## YouTube Videos\n\n")
        for i, video in enumerate(content_plan['youtube_videos'], 1):
            output.append(f"### Video {i}\n")
            output.append(f"**Title:** {video['title']}\n\n")
            output.append(f"**Description:**\n{video['description']}\n\n")
            output.append("---\n\n")
        
        return '\n'.join(output)

def main():
    """Main function to generate content"""
    generator = CrabContentGenerator()
    
    print("🦀 Crab Content Generator")
    print("=" * 50)
    
    # Generate sample content
    print("\n1. Sample X Post (Quick Tip):")
    print("-" * 50)
    print(generator.generate_x_post('quick_tip'))
    
    print("\n2. Sample X Post (Before/After):")
    print("-" * 50)
    print(generator.generate_x_post('before_after'))
    
    print("\n3. Sample Instagram Caption:")
    print("-" * 50)
    print(generator.generate_instagram_caption())
    
    print("\n4. Sample YouTube Title:")
    print("-" * 50)
    print(generator.generate_youtube_title())
    
    # Generate full week
    print("\n" + "=" * 50)
    print("Generating full week content plan...")
    week_plan = generator.generate_week_content(week_number=1)
    
    # Save as JSON
    json_path = generator.save_content_plan(week_plan)
    
    # Save as Markdown
    md_content = generator.generate_text_output(week_plan)
    md_path = Path.home() / ".openclaw" / "workspace" / "crab" / "generated_content" / "content_plan_week_1.md"
    with open(md_path, 'w') as f:
        f.write(md_content)
    print(f"✓ Markdown version saved to: {md_path}")
    
    print(f"\n📊 Week 1 Summary:")
    print(f"  - X Posts: {len(week_plan['x_posts'])}")
    print(f"  - Instagram Posts: {len(week_plan['instagram_posts'])}")
    print(f"  - YouTube Videos: {len(week_plan['youtube_videos'])}")
    print(f"\n✅ Content generation complete!")

if __name__ == '__main__':
    main()
