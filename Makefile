run_app:
	streamlit run src/streamlit/app.py

run_api:
	uvicorn src.api.fast:app --reload
