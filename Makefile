run_app:
	streamlit run streamlit_app/app.py

run_api:
	uvicorn src.api.fast:app --reload
