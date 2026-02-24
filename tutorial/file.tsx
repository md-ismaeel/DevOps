// import React from 'react'

// export default function file() {
//   return (
//     <div>file</div>
//   )
// }

// fist setup
/*
server {
    listen 80;
    listen [::]:80;
    server_name ism-dev.com;

    root /var/www/example.com;
    index index.html;

    location / {
        proxy_pass http://localhost:5000;
    }
}
*/

/*
server {
    listen 80;
    server_name ism-dev.com;

    root /var/www/example.com;
    index index.html;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
*/