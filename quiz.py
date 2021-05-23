import ipywidgets as widgets
from IPython.display import clear_output

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    layout = widgets.Layout(width='auto', height='auto') #set width and height
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        
        options = radio_options,
        description = '',
        disabled = False,
        layout = layout
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = "✅ richtig"
        else:
            s= "🚫 falsch"#"❌ falsch"
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

################################################################################

# Erste Schritte

Q1_erste_schritte = create_multipleChoice_widget('Welchen Datentyp haben die Variablen a und b?',
                                         ['Boolean',
                                          'String',
                                          'Integer',
                                          'Float'],
                                         'Integer')

Q2_erste_schritte = create_multipleChoice_widget('Was gibt das Programm zurück?',
                                         ['27',
                                          '28',
                                          '29',
                                          '30'],
                                         '28')

Q3_erste_schritte = create_multipleChoice_widget('Wie oft wird die Schleife ausgeführt?',
                                         ['gar nie',
                                          'fünfmal',
                                          'zehnmal',
                                          'vierundzwanzigmal'],
                                         'fünfmal')

Q4_erste_schritte = create_multipleChoice_widget('Was würde das Programm ausgeben, wenn in Zeile 5 ein > wäre anstelle des <= ?',
                                         ['0',
                                          '10',
                                          '28',
                                          '24'],
                                         '0')

# Arrays

Q1_arrays = create_multipleChoice_widget('Welche Werte nimmt die Laufvariable i im folgenden Loop an? for i in range(10):',
                                         ['von 0 bis und mit 10',
                                          'von 1 bis und mit 10',
                                          'von 0 bis und ohne 10',
                                          'von 1 bis und ohne 10'],
                                         'von 0 bis und ohne 10')

Q2_arrays = create_multipleChoice_widget('Welchen Wert nimmt die Laufvariable i im folgenden Loop nicht an? for i in c:',
                                         ['0',
                                          '1',
                                          '4',
                                          '5'],
                                         '0')



Q3_arrays = create_multipleChoice_widget('liste=[0 for x in range(5)] Was ist der Rückgabewert von len(liste)?',
                                         ['0',
                                          '4',
                                          '5',
                                          '6'],
                                         '5')

Q4_arrays = create_multipleChoice_widget('Wie greifen Sie auf das erste Element einer Liste liste zu?',
                                         ['liste[0]',
                                          'liste[1]',
                                          'liste(0)',
                                          'liste(1)'],
                                         'liste[0]')

Q5_arrays = create_multipleChoice_widget('Wie geben Sie eine Liste liste unter der Codezelle (oder in der Konsole) aus?',
                                         ['return liste',
                                          'output liste',
                                          'output(liste)',
                                          'print(liste)'],
                                         'print(liste)')

Q6_arrays = create_multipleChoice_widget('Was ist das Ergebnis der folgenden Rechnung: a+c[len(c)-3]*len(b)?',
                                         ['Keines, es gibt eine Fehlermeldung',
                                          '0',
                                          '5',
                                          '6'],
                                         '5')

### Algorithmen

Q1_algorithmen = create_multipleChoice_widget('Welche dieser Aktivitäten ist eher kein Algorithmus?',
                                              ['Zähneputzen.',
                                               'Schuhe binden.',
                                               'Im Fussballspiel ein Goal schiessen.', 
                                               'Schwimmen.'],
                                              'Im Fussballspiel ein Goal schiessen.')

Q2_algorithmen = create_multipleChoice_widget('Warum ist es wichtig, einen Algorithmus genau zu beschreiben?',
                                              ['Weil er sonst macht, was er will.',
                                               'Weil jederzeit klar sein muss, was zu tun ist.',
                                               'Weil die Ausführung sonst zu lange dauert.', 
                                               'Weil sonst falsche Ausgaben entstehen können.'],
                                              'Weil jederzeit klar sein muss, was zu tun ist.')
Q3_algorithmen = create_multipleChoice_widget('Wie nennt man die Eigenschaft aus der vorigen Frage?',
                                              ['Allgemeinheit',
                                               'Ausführbarkeit',
                                               'Eindeutigkeit',
                                               'Endlichkeit',
                                               'Korrektheit'],
                                              'Eindeutigkeit')

# Suchen

Q1_suchen = create_multipleChoice_widget('Schauen Sie sich die Liste a an. Welchen Suchalgorithmus würden Sie bevorzugen, um den Wert 24 zu suchen?',
                                         ['Lineare Suche',
                                          'Binäre Suche',
                                          'Beide Suchalgorithmen sind gleichermassen geeignet.',
                                          'Keiner der beiden Suchalgorithmen ist geeignet.'],
                                         'Keiner der beiden Suchalgorithmen ist geeignet.')

Q2_suchen = create_multipleChoice_widget('Schauen Sie sich die Liste b an. Welchen Suchalgorithmus würden Sie bevorzugen, um den Wert 24 zu suchen?',
                                         ['Lineare Suche',
                                          'Binäre Suche',
                                          'Beide Suchalgorithmen sind gleichermassen geeignet.',
                                          'Keiner der beiden Suchalgorithmen ist geeignet.'],
                                         'Binäre Suche')

Q3_suchen = create_multipleChoice_widget('Schauen Sie sich die Liste c an. Welchen Suchalgorithmus würden Sie bevorzugen, um den Wert 24 zu suchen?',
                                         ['Lineare Suche',
                                          'Binäre Suche',
                                          'Beide Suchalgorithmen sind gleichermassen geeignet.',
                                          'Keiner der beiden Suchalgorithmen ist geeignet.'],
                                         'Lineare Suche')

Q4_suchen = create_multipleChoice_widget('Wenn Sie den Wert 24 in der Liste b mit Hilfe der binären Suche  suchen, wieviele Schritte benötigen Sie?',
                                         ['1',
                                          '4',
                                          '5',
                                          '10'],
                                         '4')

Q5_suchen = create_multipleChoice_widget('Wenn Sie den Wert 24 in der Liste c mit Hilfe der linearen Suche suchen, wieviele Schritte benötigen Sie?',
                                         ['10',
                                          '5',
                                          '1',
                                          '0'],
                                         '1')
