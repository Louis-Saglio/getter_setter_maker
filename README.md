# getter_setter_maker
## Description :
<p>Script Python automatisant la création d'une classe Python ainsi que des instances de cette classe</p>
## Usage
<p>
    <p>Pour l'utiliser, il faut :</p>
    <ul>
        <li>Avoir les fichiers class_creator.py et getter_setter_maker.py dans le dossier courant</li>
        <li>Importer au minimum la fonction create_class_instance() du fichier getter_setter_maker.py dans le script devant l'utiliser</li>
    </ul>
</p>
### Fonctionnement de la fonction : create_class_instance()
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
### Fonctionnement de l'outil class_creator.py
<ul>
    <li>Utilité : Cet outil permet d'écrire automatiquement une classe compatible avec la fonction create_class_instance() avec sa fonction __init et ses accesseurs et mutateurs.</li>
    <li>Pour l'utiliser procédez comme il suit :
        <ul>
            <li>Placez le fichier class_creator.py là où vous voulez créer le fichier contenant votre classe</li>
            <li>Ouvrez y un invite de commande</li>
            <li>Lancez la commande suivante : C:\folder> python class_creator.py nom_de_votre_classe attribut1,attribut2,attribut3...</li>
        </ul>
    </li>
</ul>
## Problèmes connus :
<p>
<h3>Impossible d'importer une classe</h3>
<ul>
    <li>Message d'erreur : ImportError: cannot import name 'Nom_class'</li>
    <li>Cause : Cette erreur est du à un problème de cache mémoire.</li>
    <li>Solutions : Supprimer le fichier __pycache__ dans le dossier du programme; si le problème persiste redémarrer l'ordinateur.</li>
</ul>
</p>
