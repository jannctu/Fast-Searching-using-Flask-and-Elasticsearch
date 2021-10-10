# Quick start 

```
docker-compuse up -d
```
`localhost:5000`



# Install TailwindCss 

### Go to static directory 
```
cd static
```

### Setup Nodejs Env
```
npm init 
```

### Install Tailwindcss
```
npm install tailwindcss
```

### style.css 
`static\src\style.css`
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Compile Tailwindcss
```
npx tailwindcss-cli@latest build ./src/style.css -o css/main.css  
```