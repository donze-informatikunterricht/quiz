import ipywidgets as widgets
# import sys
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

## Suchen
### Insertionsort

### Selectionsort

### Bubblesort

### Mergesort

### Quicksort


## Sortieren

## Vorwissen

## Programmieren allgemein

## Listen

#for i in range(10)
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

Q6_arrays = create_multipleChoice_widget('Was ist das Ergebnis folgender Rechnung: a+c[len(c)-3]*len(b)?',
                                         ['Keines, es gibt eine Fehlermeldung',
                                          '0',
                                          '5',
                                          '6'],
                                         '5')





### Algorithmen

Q1_algorithmen = create_multipleChoice_widget('Welche Alltagsaktivität',
                                              ['Zähneputzen.',
                                               'Schuhe binden.',
                                               'Im Fussballspiel ein Goal schiessen.', 
                                               '.'],
                                              'Weil jederzeit klar sein muss, was zu tun ist.')

Q2_algorithmen = create_multipleChoice_widget('Warum ist es wichtig, einen Algorithmus genau zu beschreiben?',
                                              ['Weil er sonst macht, was er will.',
                                               'Weil jederzeit klar sein muss, was zu tun ist.',
                                               'Weil die Ausführung sonst zu lange dauert.', 
                                               'Weil sonst falsche Ausgaben entstehen können.'],
                                              'Weil jederzeit klar sein muss, was zu tun ist.')

#Q1 = create_multipleChoice_widget('blablabla',['apple','banana','pear'],'Weil die Maschine jederzeit genau wissen muss, was zu tun ist.')
#Q2 = create_multipleChoice_widget('lalalalal',['cat','dog','mouse'],'dog')
#
#Q3 = create_multipleChoice_widget('jajajajaj',['blue','white','red'],'white')