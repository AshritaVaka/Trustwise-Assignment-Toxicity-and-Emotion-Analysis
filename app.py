# # import streamlit as st
# # import requests
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import matplotlib.dates as mdates

# # API_BASE_URL = "http://localhost:5000"

# # def fetch_logs():
# #     """
# #     Fetch logs from the REST API.
# #     """
# #     response = requests.get(f"{API_BASE_URL}/logs")
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         st.error("Failed to fetch logs from the API.")
# #         return []

# # def main():
# #     st.title("Toxicity and Emotion Analysis")
    
# #     # Input section
# #     st.header("Welcome! Please add your input below to analyze")
# #     text_input = st.text_area("Enter text to analyze:")
# #     if st.button("Analyze"):
# #         if text_input.strip():
# #             # Call the API for scoring
# #             response = requests.post(f"{API_BASE_URL}/score", json={"text": text_input})
# #             if response.status_code == 200:
# #                 result = response.json()
# #                 toxicity_score = round(result['toxicity_score'], 4)
# #                 emotion_score = round(result['emotion_score'], 4)
# #                 st.success("Analysis Complete!")
# #                 st.write(f"**Toxicity Score:** {toxicity_score}")
# #                 st.write(f"**Emotion Score:** {emotion_score}")
# #             else:
# #                 st.error("Failed to analyze text.")
# #         else:
# #             st.error("Text input is required.")

# #     # Logs section
# #     st.header("Analysis Logs")
# #     logs = fetch_logs()
# #     if logs:
# #         # Convert logs to a DataFrame
# #         df = pd.DataFrame(logs)
        
# #         # Add index column
# #         df.reset_index(inplace=True)

# #         # Reorder columns
# #         df = df[["index", "id", "text", "timestamp", "emotion_score", "toxicity_score"]]

# #         # Format the timestamp to show only date, hour, and minute
# #         df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M')

# #         st.write("### Logged Results")
# #         st.dataframe(df)
        
# #         st.write("### Scores Over Time (Graph)")
# #         # Convert timestamp back to datetime for proper plotting
# #         df['timestamp'] = pd.to_datetime(df['timestamp'])

# #         # Plot toxicity and emotion scores with horizontal lines
# #         fig, ax = plt.subplots(figsize=(10, 6))
# #         ax.plot(df['timestamp'], df['toxicity_score'], label="Toxicity", color="purple")
# #         ax.plot(df['timestamp'], df['emotion_score'], label="Emotion", color="blue")
# #         ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
# #         ax.set_xlabel("Timestamp")
# #         ax.set_ylabel("Score")
# #         ax.legend()
# #         ax.set_title("Scores Over Time")
# #         st.pyplot(fig)
# #     else:
# #         st.info("No logs available.")

# # if __name__ == "__main__":
# #     main()


import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

API_BASE_URL = "http://localhost:5000"

def fetch_logs():
    """
    Fetch logs from the REST API.
    """
    response = requests.get(f"{API_BASE_URL}/logs")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch logs from the API.")
        return []

def main():
    st.title("Toxicity and Emotion Analysis")
    
    # Input section
    st.header("Welcome! Please add your input below to analyze")
    text_input = st.text_area("Enter text to analyze:")
    if st.button("Analyze"):
        if text_input.strip():
            # Call the API for scoring
            response = requests.post(f"{API_BASE_URL}/score", json={"text": text_input})
            if response.status_code == 200:
                result = response.json()
                toxicity_score = round(result['toxicity_score'], 4)
                emotion_label = result['emotion']['emotion']
                emotion_score = round(result['emotion']['score'], 4)
                st.success("Analysis Complete!")
                st.write(f"**Toxicity Score:** {toxicity_score}")
                st.write(f"**Emotion:** {emotion_label} ({emotion_score})")
            else:
                st.error("Failed to analyze text.")
        else:
            st.error("Text input is required.")

    # Logs section
    st.header("Analysis Logs")
    logs = fetch_logs()
    if logs:
        # Convert logs to a DataFrame
        df = pd.DataFrame(logs)
        
        # Add index column
        df.reset_index(inplace=True)

        # Reorder columns
        df = df[["index", "id", "text", "timestamp", "emotion_label", "emotion_score", "toxicity_score"]]

        # Format the timestamp to show only date, hour, and minute
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M')

        st.write("### Logged Results")
        st.dataframe(df)
        
        st.write("### Scores Over Time (Graph)")
        # Convert timestamp back to datetime for proper plotting
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Plot toxicity and emotion scores with horizontal lines
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['timestamp'], df['toxicity_score'], label="Toxicity", color="purple")
        ax.plot(df['timestamp'], df['emotion_score'], label="Emotion", color="blue")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("Score")
        ax.legend()
        ax.set_title("Scores Over Time")
        st.pyplot(fig)
    else:
        st.info("No logs available.")

if __name__ == "__main__":
    main()

