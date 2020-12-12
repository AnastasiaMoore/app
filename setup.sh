mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"nastyalysenkoooo@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $server.listen(process.env.PORT)\n\
" > ~/.streamlit/config.toml
