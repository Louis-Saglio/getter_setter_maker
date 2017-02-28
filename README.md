# getter_setter_maker
<p>Script Python automatisant la création d'une classe Python</p>
<p>
    <p>Pour l'utiliser, il faut :</p>
    <ul>
        <li>Avoir les fichiers class_creator.py et getter_setter_maker.py dans le dossier courant</li>
        <li>Importer au minimum la fonction create_class_instance() du fichier getter_setter_maker.py dans le script devant l'utiliser</li>
    </ul>
</p>
<p>Fonctionnement de la fonction : create_class_instance()</p>
<ul>
    <li>
        Utilité : Créer automatiquement une class avec ses méthodes de base (__init__, getter, setter) et une liste d'instance(s) de cette class suivant les paramètres choisis par l'utilisateur
    </li>
    <li>
        <p>Paramètres :</p>
        <ul>
            <li>
                Le paramètre 'nom_classe' : De type str, ce sera le nom de votre class
            </li>
            <li>
                Le paramètre 'attributs' : C'est un dictionnaire. Il correspond aux attributs de votre class et il contient également les valeurs de ces attributs pour les instances de cette class créés automatiquement.<br>
                Il doit être construit sur ce model : {"nom_attribut_1": [valeur_de_attribut_1_pour_l'instance_1, valeur_de_attribut_2_pour_l'instance_2], "nom_attribut_2": [valeur_de_attribut_2_pour_l'instance_1, valeur_de_attribut_2_pour_l'instance_2]
            </li>
        </ul>
    </li>
</ul>