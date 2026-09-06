# Python Repo

Collection of various scripts I have developed from codecademy, school, or just to mess around in my free time.

## Recipe application

The FastAPI recipe API lives in `src/tutorial_app/api`. The React client lives in
`src/tutorial_app/client`.

Run the API from the repository root:

```bash
uv run uvicorn src.tutorial_app.api.main:app --reload
```

Run the client in a second terminal:

```bash
cd src/tutorial_app/client
npm install
npm run dev
```

The Vite development server proxies `/api` requests to the FastAPI server on
`127.0.0.1:8000`.
