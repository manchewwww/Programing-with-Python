def emails_shortener(emails):
    users_for_dom = {}

    for email in emails:
        user, dom = email.split("@")
        
        if dom not in users_for_dom:
            users_for_dom[dom] = []

        users_for_dom[dom].append(user)

    result = set()

    for dom, users in users_for_dom.items():
        if len(users) == 1:
            result.add(f"{",".join(users)}@{dom}")
        else:
            result.add(f"{{{",".join(users)}}}@{dom}")

    return result

assert emails_shortener([
    "pesho@abv.bg", 
    "gosho@abv.bg",
    "sasho@abv.bg",
]) == {
    "{pesho,gosho,sasho}@abv.bg"
}

assert emails_shortener([
    "tinko@fmi.uni-sofia.bg", 
    "minko@fmi.uni-sofia.bg", 
    "pesho@pesho.org",
]) == {
    "{tinko,minko}@fmi.uni-sofia.bg", 
    "pesho@pesho.org",
}

assert emails_shortener([
    "toi_e@pesho.org",
    "golemiq@cyb.org",
]) == {
    "toi_e@pesho.org",
    "golemiq@cyb.org",
}
"✅ All OK! +1 points"