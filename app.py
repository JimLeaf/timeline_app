import streamlit as st
import json

# GitHub raw content URL
GITHUB_BASE_URL = "https://raw.githubusercontent.com/JimLeaf/timeline_app/main"

# Set page config
st.set_page_config(page_title="Site Timeline", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for styling
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f5f5f5;
    }
    
    .timeline-container {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }
    
    .event-card {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        border: 1px solid #ccc;
        padding: 15px;
        margin: 10px 0;
    }
    
    .event-header {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .event-fill {
        height: 30px;
        width: 30px;
        border-radius: 4px;
        margin-right: 15px;
    }
    
    .fill-orange { background-color: #FF9500; }
    .fill-purple { background-color: #9C27B0; }
    .fill-green { background-color: #4CAF50; }
    .fill-red { background-color: #F44336; }
    
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
    }
    
    .tag {
        display: inline-block;
        background-color: #e0e0e0;
        color: #333;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .tag.selected {
        background-color: #1897ff;
        color: white;
    }
    
    .date-range {
        color: #1897ff;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 10px;
    }
    
    .event-title {
        font-size: 18px;
        font-weight: 600;
        color: #333;
        margin-bottom: 8px;
    }
    
    .event-description {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Event data
events = [
    {
        "side": "left",
        "range": "JAN 20 - JAN 29",
        "title": "Tamamo Cross",
        "description": "Tamamo Cross is a weird horse that has **3 different position skills** in her innate kit. Her unique is mainly used for longs in terms of good proc timing so she's really just an end closer/late surger so some skills are kind of wasted. **Being specialized is better than being versatile**, oshi horse.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0120-left-1.png",
        "tags": ["PACE", "LATE", "END", "LONG", "NICHE"]
    },
    {
        "side": "right",
        "range": "JAN 20 - JAN 29",
        "title": "Nice Nature Wit & Oguri Cap Power",
        "description": "A gambler banner, Nice Nature gives **On Your Left** while Oguri gives **Furious Feat**. Both are **gambling skills for End Closers/Late Surgers primarily**. Pull if you love Lates/Ends otherwise save for major banners/horses.",
        "fills": ["fill-purple"],
        "image": f"{GITHUB_BASE_URL}/images/0120-right-1.png",
        "tags": ["LATE", "LUXURY"]
    },
    {
        "side": "left",
        "range": "JAN 27 - FEB 07",
        "title": "NY Haru Urara & NY T.M. Opera",
        "description": "NY Urara is much better than OG Urara but she is still not very strong, yet the Urara enjoyer shall want to pull this as **this will allow more Urara wins overall.** As for NY TM Opera O, **she is one of the most used parents later on and she's a solid horse that can win as well**. Her unique gives you 0.25 speed if you activate 7 skills (an easy task later on).",
        "fills": ["fill-purple", "fill-orange"],
        "image": f"{GITHUB_BASE_URL}/images/0127-left-1.png",
        "tags": ["LATE", "PACE", "DIRT", "MED", "LONG", "LUXURY", "META"]
    },
    {
        "side": "right",
        "range": "JAN 27 - FEB 07",
        "title": "Admire Vega Power & Fukukitaru Speed",
        "description": "Admire Vega Power gives **daring attack** a solid speed skill but unfortunately the card is only usable at MLB, very expensive and power cards are less than ideal because you would rather click wit than power most of the time.\n\nFukukitaru Speed is a very strong high roll card but the key word is high roll, she can **low roll very hard**. She's a friendship card in disguise who gives you a ton of stats. You can **pull her if you like to high roll** but if you rather have higher consistency pull Top Road. (Or pull both if rich)",
        "fills": ["fill-purple", "fill-orange"],
        "image": f"{GITHUB_BASE_URL}/images/0127-right-1.png",
        "tags": ["FRONT", "PACE", "LATE", "END", "LUXURY", "META"]
    },
    {
        "side": "right",
        "range": "JAN 27 - FEB 07",
        "title": "Meishi Doto Stamina Card",
        "description": "Gives Killer Tunes on a Stamina Card, really weird, stat output, not great. **Not relevant meta wise**. Free Card.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0127-right-2.png",
        "tags": ["LATE", "NICHE"]
    },
    {
        "side": "left",
        "range": "FEB 03 - FEB 12",
        "title": "Character Banner",
        "description": "It's a standard banner, what do you want?",
        "fills": ["fill-purple"],
        "image": f"{GITHUB_BASE_URL}/images/0203-left-1.png",
        "tags": ["LUXURY"]
    },
    {
        "side": "right",
        "range": "FEB 03 - FEB 12",
        "title": "S. Anshinzawa Friend & Tamamo Cross Guts",
        "description": "Anshinzawa is a **troll card**, no deck ever runs her. Tamamo Cross Guts is not a particularly significant card, no race bonus inside. Easy skip banner.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0203-right-1.png",
        "tags": ["NICHE"]
    },
    {
        "side": "left",
        "range": "FEB 07 - MAR 27",
        "title": "New Year Paid Banner (Uma)",
        "description": "Nicknamed the scam banner. You are probably getting a dupe rather than a new horse but that also depends on your number of horses owned. Pull if you want.",
        "fills": ["fill-purple"],
        "image": f"{GITHUB_BASE_URL}/images/0207-left-1.png",
        "tags": ["LUXURY"]
    },
    {
        "side": "right",
        "range": "FEB 07 - MAR 27",
        "title": "New Year Paid Banner (Support Card)",
        "description": "Nicknamed the scam banner. You are probably getting Air Shakur Wit or Goldship Stam rather than an important card. Pull if you want.",
        "fills": ["fill-purple"],
        "image": f"{GITHUB_BASE_URL}/images/0207-right-1.png",
        "tags": ["LUXURY"]
    },
    {
        "side": "left",
        "range": "FEB 09 - FEB 17",
        "title": "Sakura Chiyono O",
        "description": "A spring oriented pace/front runner, comes with speed star, spring runner and pace savvy. Nothing else particularly strong about her. **Oshi horse**.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0209-left-1.png",
        "tags": ["PACE", "NICHE", "MILE", "MEDIUM"]
    },
    {
        "side": "right",
        "range": "FEB 09 - FEB 17",
        "title": "Tazuna Friend & Riko Kashimoto Friend",
        "description": "At this point, **these cards will no longer be used** except for MLB SSR Riko because of her 10% race bonus but even then she will fall off after MANT as well. I wouldn't recommend going out of your way to get the MLB Riko, there's plenty of good banners to pull on. **Easy Skip**.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0207-right-1.png",
        "tags": ["NICHE"]
    },
    {
        "side": "left",
        "range": "FEB 15 - FEB 27",
        "title": "Val. Mihono Bourbon & Val. Eishin Flash",
        "description": "Valentine Bourbon is the **EASIEST front runner to make**, she has groundwork + front savvy + concentration + a secret event where if you get 60000 fans before valentine's day you get early lead. Meta now, falls off a bit, Meta when LoH starts.\n\nValentine Eishin Flash is **mostly just another dominator debuffer**, the other skills she has and her unique aren't much to speak about.",
        "fills": ["fill-orange", "fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0215-left-1.png",
        "tags": ["FRONT", "LATE", "MED", "META", "NICHE"]
    },
    {
        "side": "right",
        "range": "FEB 15 - FEB 27",
        "title": "Nishino Flower Wit & Sakura Baksuhin O Guts",
        "description": "Nishino Wit is **primarily used to get the gold skill downward descent**, it's really niche however, not every track has an ideal downhill.\n\nBakushin O guts has **groundwork on 1st event** and a decent sprint mid-leg gold skill.\n\nBoth of these cards don't have race bonus, not recommended since MANT is coming. **Skip**.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0215-right-1.png",
        "tags": ["PACE", "SHORT", "NICHE"]
    },
    {
        "side": "right",
        "range": "FEB 15 - FEB 27",
        "title": "Tosen Jordan SSR Speed",
        "description": "If your cards are horrible, this speed card is an F2P's lifesaver. If your cards are good enough, not relevant. **It has Breath of Fresh Air** though.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0215-right-2.png",
        "tags": ["NICHE"]
    },
    {
        "side": "left",
        "range": "FEB 23 - MAR 03",
        "title": "Mejiro Ardan",
        "description": "Primarily a pace chaser for medium, she has a unique that activates on the last straight and has race planner. **Suffers from glass legs when racing too much** which eats 10 extra energy when you race consecutively **which isn't great when MANT is coming**. **Oshi horse**.",
        "fills": ["fill-green"],
        "image": f"{GITHUB_BASE_URL}/images/0223-left-1.png",
        "tags": ["PACE", "NICHE", "MED"]
    }
]

# Get all unique tags
all_tags = set()
for event in events:
    all_tags.update(event.get("tags", []))
all_tags = sorted(list(all_tags))

# Sidebar
st.sidebar.title("🎪 Site Timeline")

# Search
search_query = st.sidebar.text_input("🔍 Search timeline...", "")

# Filters
st.sidebar.markdown("### Filters")

col1, col2 = st.sidebar.columns(2)

# Create filter columns
filter_rows = [
    ["RA", "FRONT", "PACE", "LATE", "END"],
    ["SHORT", "DIRT", "MILE", "MED", "LONG"],
    ["META", "LUXURY", "NICHE", "OSHI"]
]

selected_filters = []

for row in filter_rows:
    cols = st.sidebar.columns(len(row))
    for col, tag in zip(cols, row):
        if col.button(tag, key=f"filter_{tag}"):
            if tag not in st.session_state.get("selected_tags", []):
                if "selected_tags" not in st.session_state:
                    st.session_state["selected_tags"] = []
                st.session_state["selected_tags"].append(tag)
            else:
                st.session_state["selected_tags"].remove(tag)

if "selected_tags" not in st.session_state:
    st.session_state["selected_tags"] = []

selected_filters = st.session_state["selected_tags"]

# Clear filters button
if st.sidebar.button("Clear Filters"):
    st.session_state["selected_tags"] = []
    st.rerun()

# Main content
st.title("📅 Site Timeline")

# Legend
with st.expander("📋 LEGEND", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - 🎌 **RA**: Runaway
        - 🚀 **FRONT**: Front Runner
        - ⚡ **PACE**: Pace
        - 🐢 **LATE**: Late Surger
        - 🏁 **END**: End Closer
        """)
    with col2:
        st.markdown("""
        - 🎯 **Track Types**: SHORT, DIRT, MILE, MED, LONG
        - 💎 **Categories**: META, LUXURY, NICHE, OSHI
        """)

# Filter events
filtered_events = []
for event in events:
    # Search filter
    if search_query:
        if search_query.lower() not in event["title"].lower() and search_query.lower() not in event["description"].lower():
            continue
    
    # Tag filter
    if selected_filters:
        if not any(tag in event.get("tags", []) for tag in selected_filters):
            continue
    
    filtered_events.append(event)

# Display events
if filtered_events:
    st.markdown("---")
    
    # Group by date range
    date_ranges = {}
    for event in filtered_events:
        date_range = event["range"]
        if date_range not in date_ranges:
            date_ranges[date_range] = []
        date_ranges[date_range].append(event)
    
    # Display grouped by date
    for date_range in sorted(date_ranges.keys()):
        st.subheader(f"📍 {date_range}")
        
        left_events = [e for e in date_ranges[date_range] if e["side"] == "left"]
        right_events = [e for e in date_ranges[date_range] if e["side"] == "right"]
        
        # Display left side events
        for event in left_events:
            col1, col2 = st.columns([1, 2])
            with col2:
                with st.container(border=True):
                    # Color bars
                    color_cols = st.columns(len(event["fills"]))
                    for i, fill_class in enumerate(event["fills"]):
                        color = {
                            "fill-orange": "#FF9500",
                            "fill-purple": "#9C27B0",
                            "fill-green": "#4CAF50",
                            "fill-red": "#F44336"
                        }.get(fill_class, "#ccc")
                        color_cols[i].markdown(f'<div style="background-color: {color}; height: 20px; border-radius: 4px;"></div>', unsafe_allow_html=True)
                    
                    st.markdown(f"**{event['title']}**")
                    st.markdown(event["description"])
                    
                    # Display image if available
                    if event.get("image"):
                        st.image(event["image"], use_container_width=True)
                    
                    # Tags
                    tag_cols = st.columns(len(event.get("tags", [])))
                    for i, tag in enumerate(event.get("tags", [])):
                        is_selected = tag in selected_filters
                        tag_color = "#1897ff" if is_selected else "#e0e0e0"
                        text_color = "white" if is_selected else "#333"
                        tag_cols[i].markdown(f'<span style="display: inline-block; background-color: {tag_color}; color: {text_color}; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500;">{tag}</span>', unsafe_allow_html=True)
        
        # Display right side events
        for event in right_events:
            col1, col2 = st.columns([2, 1])
            with col1:
                with st.container(border=True):
                    # Color bars
                    color_cols = st.columns(len(event["fills"]))
                    for i, fill_class in enumerate(event["fills"]):
                        color = {
                            "fill-orange": "#FF9500",
                            "fill-purple": "#9C27B0",
                            "fill-green": "#4CAF50",
                            "fill-red": "#F44336"
                        }.get(fill_class, "#ccc")
                        color_cols[i].markdown(f'<div style="background-color: {color}; height: 20px; border-radius: 4px;"></div>', unsafe_allow_html=True)
                    
                    st.markdown(f"**{event['title']}**")
                    st.markdown(event["description"])
                    
                    # Display image if available
                    if event.get("image"):
                        st.image(event["image"], use_container_width=True)
                    
                    # Tags
                    tag_cols = st.columns(len(event.get("tags", [])))
                    for i, tag in enumerate(event.get("tags", [])):
                        is_selected = tag in selected_filters
                        tag_color = "#1897ff" if is_selected else "#e0e0e0"
                        text_color = "white" if is_selected else "#333"
                        tag_cols[i].markdown(f'<span style="display: inline-block; background-color: {tag_color}; color: {text_color}; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500;">{tag}</span>', unsafe_allow_html=True)
        
        st.markdown("---")
else:
    st.info("No events match your filters. Try adjusting your search or filters.")
