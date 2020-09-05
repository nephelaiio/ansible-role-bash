if [ -d ~/{{ bash_profile_user_path }} ]; then
    for i in ~/{{ bash_profile_user_path }}/*.sh; do
        if [ -r $i ]; then
            . $i
        fi
    done
fi
