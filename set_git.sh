echo "Setting global username to: Ex. sujitgopal880@gmail.com"
read -p "Enter Github Email id: " email_id
echo $email_id
read -p "Enter Username: " user_name
echo $user_name
git config --global user.email $email_id
git config --global user.name $user_name

echo "Congigeration secceessfull"