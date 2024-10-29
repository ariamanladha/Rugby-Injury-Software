body_parts = [
    'Head', 'Forehead', 'Temple', 'Ear', 'Eye', 'Nose', 'Mouth', 'Jaw', 'Cheek', 'Chin', 'Neck', 'Throat', 'Shoulder',
    'Upper Arm', 'Elbow', 'Forearm', 'Wrist', 'Hand', 'Fingers', 'Thumb', 'Chest', 'Ribs', 'Upper Back', 'Lower Back',
    'Abdomen', 'Groin', 'Hip', 'Thigh', 'Hamstring', 'Knee', 'Shin', 'Calf', 'Ankle', 'Heel', 'Foot', 'Toes'
]


# Common rugby injuries for each body part
common_injuries = {
    'Head': ['Concussion', 'Scalp Laceration', 'Contusion', 'Fractured Skull', 'Cervical Spine Injury'],
    'Forehead': ['Laceration', 'Contusion', 'Fracture', 'Concussion', 'Abrasion'],
    'Temple': ['Contusion', 'Laceration', 'Temple Fracture', 'Concussion', 'Temporal Arteritis'],
    'Ear': ['Auricular Hematoma', 'Laceration', 'Ruptured Eardrum', 'Tinnitus', 'Ear Avulsion'],
    'Eye': ['Corneal Abrasion', 'Conjunctivitis', 'Orbital Fracture', 'Retinal Detachment', 'Hyphema'],
    'Nose': ['Nasal Fracture', 'Epistaxis (Nosebleed)', 'Nasal Septum Hematoma', 'Rhinorrhea', 'Laceration'],
    'Mouth': ['Dental Avulsion', 'Laceration', 'Jaw Fracture', 'Tooth Fracture', 'Oral Hematoma'],
    'Jaw': ['Mandibular Fracture', 'Dislocated Jaw', 'TMJ Dysfunction', 'Laceration', 'Jaw Contusion'],
    'Cheek': ['Cheekbone Fracture', 'Contusion', 'Laceration', 'Zygomatic Arch Fracture', 'Facial Nerve Injury'],
    'Chin': ['Laceration', 'Fracture', 'Contusion', 'Mandibular Dislocation', 'Dental Injury'],
    'Neck': ['Cervical Sprain', 'Cervical Fracture', 'Strangulation Injury', 'Whiplash', 'Cervical Disc Injury'],
    'Throat': ['Laryngeal Fracture', 'Throat Contusion', 'Laryngospasm', 'Pharyngeal Laceration', 'Esophageal Injury'],
    'Shoulder': ['Dislocation', 'AC Joint Injury', 'Rotator Cuff Tear', 'Clavicle Fracture', 'Shoulder Impingement Syndrome'],
    'Upper Arm': ['Humerus Fracture', 'Bicep Tendonitis', 'Tricep Tendonitis', 'Contusion', 'Muscle Strain'],
    'Elbow': ['Fracture', 'Dislocation', 'Olecranon Bursitis', 'Ulnar Nerve Entrapment', 'Tendonitis'],
    'Forearm': ['Radius Fracture', 'Ulna Fracture', 'Compartment Syndrome', 'Forearm Strain', 'Deep Contusion'],
    'Wrist': ['Fracture', 'Sprain', 'Carpal Tunnel Syndrome', 'Ganglion Cyst', 'TFCC Injury'],
    'Hand': ['Fracture', 'Dislocation', 'Laceration', 'Tendon Injury', 'Crush Injury'],
    'Fingers': ['Fracture', 'Dislocation', 'Mallet Finger', 'Jersey Finger', 'Boutonniere Deformity'],
    'Thumb': ['Fracture', 'Sprain', 'Skier’s Thumb', 'Thumb Dislocation', 'Arthritis'],
    'Chest': ['Rib Fracture', 'Sternal Fracture', 'Costochondritis', 'Pectoral Muscle Strain', 'Contusion'],
    'Ribs': ['Rib Fracture', 'Costochondral Separation', 'Muscle Strain', 'Contusion', 'Pneumothorax'],
    'Upper Back': ['Muscle Strain', 'Thoracic Spine Injury', 'Fracture', 'Contusion', 'Herniated Disc'],
    'Lower Back': ['Lumbar Strain', 'Herniated Disc', 'Sciatica', 'Spondylolisthesis', 'Spinal Fracture'],
    'Abdomen': ['Muscle Strain', 'Contusion', 'Hernia', 'Organ Injury', 'Abdominal Wall Tear'],
    'Groin': ['Groin Strain', 'Hernia', 'Testicular Contusion', 'Adductor Tendonitis', 'Labral Tear'],
    'Hip': ['Hip Dislocation', 'Hip Pointer', 'Hip Labral Tear', 'Hip Flexor Strain', 'Femoral Neck Fracture'],
    'Thigh': ['Quadriceps Strain', 'Hamstring Strain', 'Contusion', 'Muscle Rupture', 'Femoral Fracture'],
    'Hamstring': ['Hamstring Strain', 'Hamstring Tear', 'Avulsion Fracture', 'Tendonitis', 'Sciatica'],
    'Knee': ['ACL Injury', 'MCL Injury', 'Meniscus Tear', 'Patellar Fracture', 'Tendonitis'],
    'Shin': ['Shin Splints', 'Compartment Syndrome', 'Stress Fracture', 'Deep Vein Thrombosis', 'Contusion'],
    'Calf': ['Calf Strain', 'Calf Tear', 'Baker’s Cyst', 'Compartment Syndrome', 'Deep Vein Thrombosis'],
    'Ankle': ['Sprain', 'Fracture', 'Achilles Tendonitis', 'Ankle Impingement', 'Pott’s Fracture'],
    'Heel': ['Plantar Fasciitis', 'Heel Spur', 'Achilles Tendonitis', 'Bursitis', 'Stress Fracture'],
    'Foot': ['Fracture', 'Sprain', 'Plantar Fasciitis', 'Metatarsalgia', 'Bunion'],
    'Toes': ['Fracture', 'Dislocation', 'Gout', 'Ingrown Toenail', 'Bunion']
}

symptoms = {
    'Concussion': ['Headache', 'Confusion', 'Dizziness', 'Nausea', 'Sensitivity to light'],
    'Scalp Laceration': ['Bleeding from scalp', 'Visible cut on the scalp', 'Swelling', 'Tenderness'],
    'Contusion': ['Bruising', 'Swelling', 'Pain on touch', 'Discoloration'],
    'Fractured Skull': ['Severe headache', 'Bleeding from ears/nose', 'Bruising around eyes', 'Confusion', 'Seizures'],
    'Cervical Spine Injury': ['Neck pain', 'Loss of sensation in limbs', 'Muscle weakness', 'Difficulty breathing'],
    'Laceration': ['Bleeding', 'Visible cut', 'Tenderness', 'Swelling'],
    'Temple Fracture': ['Headache', 'Bruising around eyes', 'Nausea', 'Confusion'],
    'Auricular Hematoma': ['Swelling of the ear', 'Pain in the ear', 'Bruising'],
    'Corneal Abrasion': ['Eye pain', 'Tearing', 'Redness', 'Blurred vision'],
    'Nasal Fracture': ['Nose pain', 'Swelling', 'Bruising around nose', 'Bleeding'],
    'Dental Avulsion': ['Missing tooth', 'Bleeding gums', 'Pain'],
    'Mandibular Fracture': ['Jaw pain', 'Swelling', 'Bruising', 'Difficulty speaking'],
    'Cervical Sprain': ['Neck pain', 'Stiffness', 'Decreased range of motion'],
    'Shoulder Dislocation': ['Shoulder pain', 'Visible deformity', 'Swelling'],
    'Bicep Tendonitis': ['Pain in front of shoulder', 'Weakness', 'Tenderness'],
    'Elbow Fracture': ['Elbow pain', 'Swelling', 'Bruising', 'Difficulty moving'],
    'Radius Fracture': ['Forearm pain', 'Swelling', 'Bruising'],
    'Wrist Sprain': ['Wrist pain', 'Swelling', 'Difficulty moving wrist'],
    'Hand Fracture': ['Hand pain', 'Swelling', 'Bruising'],
    'Finger Fracture': ['Finger pain', 'Swelling', 'Bruising', 'Difficulty moving finger'],
    'Thumb Sprain': ['Thumb pain', 'Swelling', 'Difficulty gripping'],
    'Rib Fracture': ['Rib pain', 'Difficulty breathing', 'Swelling'],
    'Lumbar Strain': ['Lower back pain', 'Stiffness', 'Decreased range of motion'],
    'Hip Dislocation': ['Hip pain', 'Visible deformity', 'Difficulty moving leg'],
    'Quadriceps Strain': ['Thigh pain', 'Swelling', 'Bruising'],
    'ACL Injury': ['Knee pain', 'Swelling', 'Instability', 'Difficulty walking'],
    'Shin Splints': ['Shin pain', 'Swelling', 'Tenderness'],
    'Calf Strain': ['Calf pain', 'Swelling', 'Bruising'],
    'Ankle Sprain': ['Ankle pain', 'Swelling', 'Bruising', 'Difficulty walking'],
    'Plantar Fasciitis': ['Heel pain', 'Tenderness', 'Stiffness'],
    'Toe Fracture': ['Toe pain', 'Swelling', 'Bruising', 'Difficulty moving toe']
    # Add additional injuries and their symptoms here as needed
}

def not_sure_flow():
    print("You selected 'Not sure'. Please list your symptoms from the following options:")
    all_symptoms = {symptom for symptoms_list in symptoms.values() for symptom in symptoms_list}
    for symptom in all_symptoms:
        print(symptom)
    user_symptoms = input("Enter your symptoms separated by commas: ").split(',')

    possible_injuries = {}
    for injury, injury_symptoms in symptoms.items():
        match_count = len(set(user_symptoms) & set(injury_symptoms))
        if match_count > 0:
            possible_injuries[injury] = match_count

    if not possible_injuries:
        print("No matching injuries found for the given symptoms.")
        return

    most_likely_injury = max(possible_injuries, key=possible_injuries.get)
    print(f"The most likely injury based on your symptoms is: {most_likely_injury}")

    treatment_steps = injury_treatment.get(most_likely_injury, ["No treatment recommendation available for this injury."])
    print("\nFollow these steps to treat your injury:")
    for step in treatment_steps:
        print(step)


injury_treatment = {
    'Concussion': [
        'Rest and avoid activities that require concentration.',
        'Avoid physical activity until cleared by a medical professional.',
        'Take pain relievers if necessary.',
        'Consult with a healthcare provider immediately.',
        'Gradually return to activities as symptoms allow under medical supervision.'
    ],
    'Scalp Laceration': [
        'Apply direct pressure to stop bleeding.',
        'Clean the wound with water and mild soap.',
        'Apply an antibiotic ointment to prevent infection.',
        'Cover the wound with a sterile bandage.',
        'Seek medical attention if the laceration is deep, bleeding does not stop, or signs of infection appear.'
    ],
    'Contusion': [
        'Rest the injured area.',
        'Apply ice wrapped in a cloth for short periods to reduce swelling.',
        'Use a compression bandage to minimize swelling.',
        'Elevate the injured area above heart level if possible.',
        'Seek medical attention if pain is severe or if the contusion does not improve.'
    ],
    'Fractured Skull': [
        'Do not move the person unless necessary to avoid further injury.',
        'Stop any bleeding by applying a sterile or clean cloth.',
        'Do not apply direct pressure if you suspect a skull fracture.',
        'Do not remove any objects stuck in the wound.',
        'Seek immediate medical attention.'
    ],
    'Cervical Spine Injury': [
        'Do not move the injured person to avoid further damage.',
        'Keep the person still and wait for emergency medical personnel.',
        'If the person must vomit, keep their neck and back straight while turning their entire body to the side.',
        'Do not remove any helmet or other sports gear.',
        'Stabilize the neck if trained to do so.'
    ],
    'Forehead Laceration': [
        'Apply pressure to control bleeding.',
        'Clean the area with mild soap and water.',
        'Use a sterile bandage to cover the wound.',
        'Apply ice to reduce swelling.',
        'Seek medical attention if the wound is deep or if there is a concern for scarring.'
    ],
    'Forehead Contusion': [
        'Apply ice to the area to reduce swelling.',
        'Keep the area elevated if possible.',
        'Monitor for signs of concussion or other serious injury.',
        'Use over-the-counter pain medication if necessary.',
        'Seek medical attention if symptoms worsen or do not improve.'
    ],
    'Forehead Fracture': [
        'Immobilize the head and neck.',
        'Apply ice to control swelling.',
        'Seek immediate medical attention.',
        'Avoid placing pressure on the fractured area.',
        'Prepare for possible surgery, depending on the severity of the fracture.'
    ],
    'Forehead Concussion': [
        'Rest and limit activities that require mental or physical exertion.',
        'Monitor symptoms closely for any signs of worsening.',
        'Consult a healthcare provider for a full evaluation.',
        'Avoid activities that risk additional head injury.',
        'Follow a graduated return to normal activities as approved by a healthcare professional.'
    ],
    'Forehead Abrasion': [
        'Clean the area with mild soap and water.',
        'Apply an antibiotic ointment to prevent infection.',
        'Cover with a sterile bandage.',
        'Change the bandage daily and monitor for signs of infection.',
        'Seek medical attention if the abrasion is severe or not healing.'
    ],
    'Temple Contusion': [
        'Apply ice to the area for short periods of time.',
        'Rest and avoid strenuous activities.',
        'Monitor for any cognitive or neurological changes.',
        'Use pain relievers as needed.',
        'Seek medical care if there are concerns about a more serious injury.'
    ],
    'Temporal Arteritis': [
    'Seek immediate medical attention, especially if experiencing vision changes or pain.',
    'Expect to undergo blood tests and possibly imaging to confirm diagnosis.',
    'Follow prescribed steroid treatment to reduce artery inflammation.',
    'Regular follow-up with a healthcare provider is necessary to monitor the condition.',
    'Avoid smoking, as it can aggravate the condition.'
],
    'Temple Laceration': [
        'Apply direct pressure to the laceration to stop bleeding.',
        'Clean the wound with sterile water or saline solution.',
        'Seek medical attention for wound assessment and possible suturing.',
        'Watch for signs of infection such as redness, swelling, or discharge.',
        'Follow up with healthcare provider as recommended.'
    ],

    'Temple Fracture': [
        'Do not apply direct pressure to the fracture site to avoid aggravating any injury.',
        'Immobilize the head and neck until medical help is available.',
        'Apply ice to the surrounding area to reduce swelling, avoiding direct contact with the fracture site.',
        'Seek immediate medical attention for proper imaging and assessment.',
        'Follow medical advice which may include surgery or specific headgear for protection during healing.'
    ],

    'Concussion (Forehead/Temple)': [
        'Cease any current activities and rest.',
        'Monitor for any symptoms such as headaches, dizziness, nausea, or changes in consciousness.',
        'Consult a healthcare provider as soon as possible for an evaluation.',
        'Follow a gradual return to activities only after medical clearance.',
        'Watch for any late-appearing symptoms and seek re-evaluation if they occur.'
    ],

    'Abrasion (Forehead/Temple)': [
        'Clean the area gently with mild soap and water, being careful not to rub the wound.',
        'Apply an antibiotic ointment to prevent infection.',
        'Cover the area with a clean bandage or dressing.',
        'Change the dressing daily and watch for signs of infection.',
        'If the abrasion is extensive or not healing, seek medical advice.'
    ],
    'Auricular Hematoma': [
        'Apply ice to the ear to reduce swelling.',
        'Avoid any activity that could worsen the hematoma.',
        'Seek medical attention as draining the hematoma might be necessary.',
        'Use headgear to protect the ear during future activities once healed.'
    ],
    'Ear Laceration': [
        'Apply pressure to stop any bleeding.',
        'Clean the laceration with sterile water or saline.',
        'Cover with a clean, dry dressing.',
        'Seek medical attention, especially if the laceration is deep or if there is concern about hearing loss.'
    ],
    'Ruptured Eardrum': [
        'Keep the ear dry by avoiding swimming and using a shower cap while bathing.',
        'Avoid inserting anything into the ear, including cotton swabs.',
        'Use over-the-counter pain relievers to manage pain if necessary.',
        'Consult a healthcare provider for evaluation and possible antibiotic treatment to prevent infection.'
    ],
    'Tinnitus': [
        'Reduce exposure to loud noises to prevent worsening of symptoms.',
        'Use white noise or background sound to help mask the ringing.',
        'Avoid stimulants such as caffeine and nicotine which can aggravate tinnitus.',
        'Seek medical advice, especially if the tinnitus is sudden, persistent, or associated with hearing loss.'
    ],
    'Ear Avulsion': [
        'Apply pressure to control bleeding without pressing on the avulsed part.',
        'Preserve the avulsed part by wrapping it in moist gauze and sealing it in a plastic bag placed on ice.',
        'Do not delay medical treatment; time is critical for the possibility of reattachment surgery.'
    ],
    'Corneal Abrasion': [
        'Do not rub the eye; keep it closed or lightly covered with a sterile dressing.',
        'Blink several times or rinse the eye with clean water or saline solution.',
        'Seek medical attention for an appropriate examination and treatment.',
        'Avoid wearing contact lenses until cleared by a healthcare provider.'
    ],
    'Conjunctivitis': [
        'Avoid touching or rubbing the affected eye.',
        'Apply a cool or warm compress to soothe irritation.',
        'Use antibiotic or antihistamine eye drops if prescribed by a healthcare provider.',
        'Maintain good hygiene, like washing hands frequently, to prevent spreading or reinfection.'
    ],
    'Orbital Fracture': [
        'Apply ice to the affected area to reduce swelling.',
        'Avoid blowing the nose, which can cause further complications.',
        'Seek immediate medical attention for proper imaging and assessment.',
        'Surgery may be required depending on the severity of the fracture.'
    ],
    'Retinal Detachment': [
        'Seek immediate medical attention as this is a surgical emergency.',
        'Do not engage in activities that involve moving the head or eyes vigorously.',
        'Prior to medical care, avoid taking medications that may thin the blood, like aspirin, unless prescribed.'
    ],
    'Hyphema': [
        'Cover the eye with a protective shield.',
        'Do not apply pressure to the eye.',
        'Elevate the head to help reduce pressure in the eye.',
        'Seek immediate medical attention as this condition can lead to permanent vision loss.'
    ],
    'Nasal Fracture': [
        'Apply a cold compress to reduce swelling and pain.',
        'Keep the head elevated, especially when sleeping, to decrease bleeding and swelling.',
        'Do not attempt to straighten the nose if deformed.',
        'Seek medical attention for proper alignment and to check for other injuries.'
    ],
    'Epistaxis (Nosebleed)': [
        'Sit upright and lean forward slightly to prevent swallowing blood.',
        'Pinch the soft part of the nose and hold for 10 to 15 minutes.',
        'Apply a cold compress to the nose and cheeks.',
        'If bleeding does not stop after 20 minutes, seek medical attention.'
    ],
    'Nasal Septum Hematoma': [
        'Seek immediate medical attention as drainage might be necessary.',
        'Do not blow the nose or insert anything into the nostrils.',
        'Follow up with an otolaryngologist (ENT specialist) as instructed.'
    ],
    'Rhinorrhea': [
        'Stay hydrated and rest.',
        'Use over-the-counter decongestants or antihistamines if appropriate.',
        'If symptoms persist or are accompanied by other symptoms like facial pain, seek medical advice.'
    ],
    'Nose Laceration': [
        'Apply direct pressure to control bleeding.',
        'Clean the laceration with water and mild soap.',
        'Seek medical attention for wound assessment and possible closure.', 'Monitor for signs of infection.'
    ],
    'Dental Avulsion': [
        'Handle the avulsed tooth by the crown, not the root.',
        'If the tooth is dirty, wash it briefly (10 seconds) under cold running water and reposition it. Try to encourage the patient/parent to replant the tooth. Otherwise, store it in a suitable medium (milk or saliva).',
        'Seek emergency dental treatment immediately.'
    ],
    'Mouth Laceration': [
        'Rinse the mouth with mild saline water or antiseptic mouthwash.',
        'Apply pressure using gauze to control bleeding.',
        'Avoid eating hard, spicy, or hot food that can irritate the wound.',
        'Seek medical attention if the laceration is deep, to determine if sutures are needed.'
    ],
    'Jaw Fracture': [
        'Immobilize the jaw and do not attempt to move it.',
        'Apply ice to the sides of the face to reduce swelling.',
        'Seek immediate medical attention as surgery may be required.',
        'Maintain a soft or liquid diet as advised by a healthcare provider.'
    ],
    'Tooth Fracture': [
        'Rinse the mouth with warm water.',
        'Apply a cold pack to the cheek to reduce swelling.',
        'Locate and save any broken tooth fragments.',
        'Seek prompt dental attention.'
    ],
    'Oral Hematoma': [
        'Apply ice to the area to limit swelling.',
        'Avoid hot foods or beverages which can increase bleeding.',
        'Do not puncture or try to drain the hematoma.',
        'Seek medical attention if the hematoma is large or painful, as it may need to be drained by a healthcare professional.'
    ],
    'Mandibular Fracture': [
        'Keep the head elevated and apply ice to control swelling.',
        'Use a bandage wrapped beneath the jaw and over the top of the head to stabilize the jaw.',
        'Consume only soft foods and avoid any jaw movements.',
        'Seek immediate medical attention for proper treatment, which may include surgery.'
    ],
    'Dislocated Jaw': [
        'Support the jaw to prevent it from moving.',
        'Apply ice to relieve pain and reduce swelling.',
        'Do not attempt to force the jaw back into place yourself.',
        'Seek immediate medical care to have the jaw properly repositioned.'
    ],
    'TMJ Dysfunction': [
        'Eat soft foods to minimize jaw movement.',
        'Use hot or cold packs to reduce pain and swelling.',
        'Perform gentle jaw-stretching exercises if recommended by a healthcare professional.',
        'Avoid excessive jaw movements such as yawning or chewing gum.'
    ],
    'Jaw Laceration': [
        'Clean the area gently and apply pressure with a clean cloth to control bleeding.',
        'Seek medical attention to determine if sutures are necessary.',
        'Be aware of the risk of infection, and follow care instructions provided by a healthcare provider.'
    ],
    'Jaw Contusion': [
        'Apply ice to the jaw area to help reduce swelling.',
        'Take over-the-counter pain medication to manage discomfort.',
        'Eat soft foods and avoid chewing on the side where the contusion occurred.',
        'If pain or swelling persists, seek medical evaluation.'
    ],
    'Cheekbone Fracture': [
        'Apply ice to the cheek area to control swelling.',
        'Avoid blowing the nose or anything that could cause further displacement.',
        'Seek immediate medical attention for appropriate imaging and management.',
        'Surgery may be required depending on the severity of the fracture.'
    ],
    'Cheek Contusion': [
        'Use ice wrapped in a cloth to apply to the cheek sparingly.',
        'Rest and avoid strenuous activity to let the injury heal.',
        'If there is significant swelling or pain, consult a healthcare provider.'
    ],
    'Cheek Laceration': [
        'Apply direct pressure with a clean cloth to control bleeding.',
        'Clean the area with sterile water or saline solution.',
        'Seek medical attention for wound assessment and possible suturing.'
    ],
    'Zygomatic Arch Fracture': [
        'Do not apply pressure to the affected area.',
        'Apply ice to reduce pain and swelling.',
        'Seek medical attention for a full evaluation and treatment plan.',
        'Avoid activities that may risk further injury to the face.'
    ],
    'Facial Nerve Injury': [
        'Seek medical attention to determine the extent of the injury.',
        'Follow the healthcare provider’s instructions, which may include medications or physical therapy.',
        'Protect the eye if the eyelid cannot close properly, using lubricating eye drops or an eye patch.'
    ],
    'Chin Laceration': [
        'Clean the wound with mild soap and water.',
        'Apply direct pressure with a sterile cloth to stop any bleeding.',
        'Seek medical attention to determine if stitches are required.',
        'Monitor for signs of infection, such as redness, swelling, or pus.'
    ],
    'Chin Fracture': [
        'Apply ice to reduce swelling.',
        'Keep the head and neck immobilized.',
        'Seek immediate medical care for proper diagnosis and treatment.',
        'Follow a soft diet to avoid stress on the jaw.'
    ],
    'Chin Contusion': [
        'Apply ice to the affected area to minimize swelling.',
        'Use over-the-counter pain relievers to manage discomfort.',
        'If swelling does not decrease, seek medical attention.'
    ],
    'Mandibular Dislocation': [
        'Support the jaw to prevent further movement.',
        'Apply ice to relieve pain and reduce swelling.',
        'Seek immediate medical attention to have the jaw repositioned.'
    ],
    'Dental Injury': [
        'Rinse the mouth with warm water.',
        'Apply gauze to any bleeding areas.',
        'Save any broken teeth or parts and bring them to a dentist immediately.',
        'Use a cold compress to ease pain and swelling.',
        'Visit a dentist as soon as possible for further treatment.'
    ],
    'Cervical Sprain': [
        'Rest the neck and avoid sudden movements.',
        'Apply ice to reduce pain and swelling.',
        'Consider wearing a soft cervical collar for comfort.',
        'Use over-the-counter pain relievers if necessary.',
        'Seek medical attention if symptoms persist or worsen.'
    ],
    'Cervical Fracture': [
        'Do not move the person unless absolutely necessary.',
        'Immobilize the neck until emergency personnel arrive.',
        'Apply ice packs to control swelling.',
        'Seek immediate medical attention.'
    ],
    'Strangulation Injury': [
        'Call emergency services immediately.',
        'Do not remove any objects constricting the neck.',
        'Loosen any tight clothing around the neck.',
        'Monitor breathing and be prepared to start CPR if necessary.'
    ],
    'Whiplash': [
        'Rest the neck and avoid quick movements.',
        'Apply ice for the first 24 hours to reduce swelling, then switch to heat.',
        'Use over-the-counter pain relievers and muscle relaxants as needed.',
        'Consider physical therapy exercises to strengthen neck muscles.'
    ],
    'Cervical Disc Injury': [
        'Rest and avoid activities that worsen pain.',
        'Apply heat or ice to the affected area.',
        'Take over-the-counter pain medication.',
        'Seek medical attention for further evaluation and treatment options such as physical therapy or surgery.'
    ],
    'Laryngeal Fracture': [
        'Seek immediate medical attention as this is an emergency.',
        'Avoid speaking or coughing excessively.',
        'Maintain an upright position to ease breathing.',
        'Be prepared for emergency intervention to secure the airway.'
    ],
    'Throat Contusion': [
        'Apply ice to the neck area to reduce swelling.',
        'Monitor for difficulty breathing or swallowing.',
        'Seek medical attention if symptoms are severe or if breathing is compromised.'
    ],
    'Laryngospasm': [
        'Stay calm and try to breathe slowly and deeply.',
        'Inhale moist air or steam to help relax the vocal cords.',
        'Seek medical attention if breathing does not return to normal quickly.'
    ],
    'Pharyngeal Laceration': [
        'Apply pressure if there is external bleeding.',
        'Do not eat or drink if there is a suspicion of internal injury.',
        'Seek immediate medical attention for assessment and treatment.'
    ],
    'Esophageal Injury': [
        'Do not eat or drink if an esophageal injury is suspected.',
        'Seek immediate medical attention.',
        'Surgery may be required depending on the severity of the injury.'
    ],
    'Shoulder Dislocation': [
        'Immobilize the shoulder.',
        'Apply ice to reduce pain and swelling.',
        'Seek medical attention for proper repositioning and immobilization.',
        'Follow up with physical therapy to restore function and strength.'
    ],
    'AC Joint Injury': [
        'Rest the shoulder and avoid movements that cause pain.',
        'Apply ice to the affected area.',
        'Use a sling to immobilize the shoulder if necessary.',
        'Consider seeing a specialist for severe injuries which may require surgery.'
    ],
        'Rotator Cuff Tear': [
        'Rest the shoulder and avoid activities that cause pain.',
        'Apply ice to reduce inflammation.',
        'Use over-the-counter pain medication to alleviate discomfort.',
        'Engage in physical therapy exercises to improve flexibility and strengthen shoulder muscles.',
        'In severe cases, consult with a healthcare provider about the possibility of surgery.'
    ],
    'Clavicle Fracture': [
        'Immobilize the arm using a sling.',
        'Apply ice wrapped in a cloth to the injured area to reduce pain and swelling.',
        'Take over-the-counter pain relievers as recommended by a healthcare provider.',
        'Seek medical attention for proper diagnosis and treatment which may include wearing a brace or surgery.'
    ],
    'Shoulder Impingement Syndrome': [
        'Rest the shoulder and avoid overhead activities.',
        'Apply ice to the shoulder to reduce pain and swelling.',
        'Perform gentle stretching and strengthening exercises as recommended by a healthcare provider.',
        'In some cases, a steroid injection or surgery may be necessary.'
    ],
    'Humerus Fracture': [
        'Immobilize the arm and apply ice to reduce swelling.',
        'Seek medical attention for proper splinting or casting.',
        'Surgery may be required for severe fractures.',
        'Physical therapy will be necessary for rehabilitation post-healing.'
    ],
    'Bicep Tendonitis': [
        'Rest the arm and avoid activities that exacerbate the pain.',
        'Apply ice to the affected area to reduce inflammation.',
        'Consider using anti-inflammatory medications as recommended by a healthcare provider.',
        'Engage in stretching and strengthening exercises once pain subsides.'
    ],
    'Tricep Tendonitis': [
        'Rest the arm to avoid further strain.',
        'Apply ice to the affected area after activity to reduce pain and swelling.',
        'Use over-the-counter pain relief or anti-inflammatory medications if needed.',
        'Physical therapy may be beneficial for recovery.'
    ],
    'Upper Arm Contusion': [
        'Apply ice to the injured area to minimize swelling.',
        'Rest the arm and avoid strenuous activities.',
        'Use a compression bandage to support the arm if necessary.',
        'If pain and swelling do not subside, seek medical evaluation.'
    ],
    'Muscle Strain': [
        'Rest the affected muscle and avoid activities that cause pain.',
        'Apply ice to the area for the first 24-48 hours to reduce swelling.',
        'Use a compression bandage and elevate the arm to reduce swelling.',
        'Gradually stretch and strengthen the muscle as part of rehabilitation.'
    ],
    'Elbow Fracture': [
        'Immobilize the elbow and apply ice to control swelling.',
        'Seek immediate medical care to assess the need for a cast or surgery.',
        'Keep the elbow elevated above heart level to minimize swelling.',
        'Follow up with physical therapy for joint mobility and muscle strength.'
    ],
    'Elbow Dislocation': [
        'Do not attempt to move or reduce the dislocation yourself.',
        'Immobilize the elbow and apply ice to reduce pain and swelling.',
        'Seek emergency medical attention for proper repositioning.',
        'Physical therapy will be necessary after the elbow is stabilized.'
    ],
    'Olecranon Bursitis': [
        'Avoid leaning on the affected elbow.',
        'Apply ice and use anti-inflammatory medications to reduce pain and swelling.',
        'If the bursitis is caused by an infection, seek medical attention for antibiotic treatment.',
        'Aspiration of the bursa fluid may be necessary for persistent cases.'
    ],
    'Ulnar Nerve Entrapment': [
        'Rest the elbow and avoid activities that cause numbness or pain.',
        'Apply ice to the area to reduce swelling.',
        'Use over-the-counter pain relievers and anti-inflammatory medications as needed.',
        'Consider wearing an elbow brace at night to prevent over-bending.',
        'Physical therapy may be recommended to relieve pressure on the nerve.'
    ],
    'Elbow Tendonitis': [
        'Rest the elbow and avoid repetitive movements.',
        'Apply ice to the area after activity.',
        'Use over-the-counter anti-inflammatory medications if needed.',
        'Physical therapy exercises can help relieve pain and restore function.'
    ],
    'Radius Fracture': [
        'Immobilize the arm and apply ice to the injured area.',
        'Seek medical attention for proper diagnosis and treatment.',
        'A splint or cast may be necessary to ensure proper healing.',
        'Physical therapy may be recommended to regain strength and mobility.'
    ],
    'Ulna Fracture': [
        'Immobilize the forearm and apply ice to reduce swelling.',
        'Seek medical care to determine if casting or surgery is required.',
        'Elevate the arm to decrease swelling.',
        'Rehabilitation exercises will be necessary for recovery.'
    ],
    'Compartment Syndrome': [
        'Recognize this as a medical emergency and seek immediate care.',
        'Do not apply ice or compression, as this can worsen the condition.',
        'Surgery may be required to relieve pressure and prevent muscle and nerve damage.'
    ],
    'Forearm Strain': [
        'Rest the forearm and avoid activities that increase pain.',
        'Apply ice to the affected area for 20 minutes at a time.',
        'Use a compression bandage to support the forearm.',
        'Gentle stretching and strengthening exercises can aid in recovery.'
    ],
    'Deep Contusion': [
        'Rest the affected area and protect it from further injury.',
        'Apply ice to reduce pain and swelling.',
        'Use a compression wrap to minimize swelling.',
        'If the contusion is severe or if you suspect a more serious injury, seek medical evaluation.'
    ],
    'Wrist Fracture': [
        'Immobilize the wrist and apply ice to reduce swelling.',
        'Seek medical attention for proper diagnosis and treatment; a cast or splint may be necessary.',
        'Follow up with physical therapy to restore range of motion and strength after immobilization.'
    ],
    'Wrist Sprain': [
        'Rest the wrist and apply ice to reduce pain and swelling.',
        'Use a compression bandage to support the wrist.',
        'Keep the wrist elevated above the heart level.',
        'For severe sprains, seek medical attention for potential immobilization or physical therapy.'
    ],
    'Carpal Tunnel Syndrome': [
        'Rest the wrist and avoid activities that may worsen symptoms.',
        'Apply ice to reduce swelling and use wrist splints to immobilize the wrist, especially at night.',
        'Over-the-counter anti-inflammatory medications may help relieve pain.',
        'If symptoms persist, consult a healthcare provider for other treatments such as corticosteroid injections or surgery.'
    ],
    'Ganglion Cyst': [
        'Avoid repetitive wrist movements that may exacerbate the cyst.',
        'Apply ice if the cyst causes pain.',
        'Wear a wrist brace or splint to immobilize the area if necessary.',
        'If the cyst is painful or interferes with wrist movement, seek medical advice for potential aspiration or removal.'
    ],
    'TFCC Injury': [
        'Rest the wrist and limit movements that cause pain.',
        'Apply ice to the affected area to manage pain and swelling.',
        'Use a wrist splint or brace to immobilize the wrist and allow the TFCC to heal.',
        'Consult a healthcare provider for the appropriate treatment plan, which may include physical therapy or surgery for severe injuries.'
    ],
    'Hand Fracture': [
        'Immobilize the hand with a splint or cast.',
        'Apply ice to reduce swelling and pain.',
        'Keep the hand elevated, especially in the first 48 hours.',
        'Seek medical attention for proper diagnosis and treatment.'
    ],
    'Hand Dislocation': [
        'Do not attempt to put the dislocation back in place.',
        'Immobilize the hand and apply ice to ease pain and swelling.',
        'Seek professional medical treatment for reduction and splinting.'
    ],
    'Hand Laceration': [
        'Control bleeding by applying direct pressure with a clean cloth.',
        'Clean the wound thoroughly to prevent infection.',
        'Seek medical attention for possible suturing and further care.'
    ],
    'Hand Tendon Injury': [
        'Immobilize the hand and avoid using it to prevent further injury.',
        'Apply ice to minimize swelling.',
        'Seek medical attention for a precise diagnosis, as surgery may be necessary.'
    ],
    'Crush Injury': [
        'Remove any jewelry from the affected hand immediately.',
        'Avoid moving the hand and keep it elevated.',
        'Cover the area with a clean cloth and apply ice if possible.',
        'Seek emergency medical care, as crush injuries can be severe and require immediate treatment.'
    ],
    'Finger Fracture': [
        'Immobilize the finger using a splint.',
        'Apply ice to the area to reduce pain and swelling.',
        'Keep the hand elevated above heart level.',
        'Seek medical attention to ensure proper healing.'
    ],
    'Finger Dislocation': [
        'Immobilize the finger and apply ice.',
        'Do not try to correct the dislocation yourself.',
        'Seek medical attention to have the dislocation reduced safely.'
    ],
    'Mallet Finger': [
        'Use a splint to keep the finger straight at all times.',
        'Apply ice to reduce swelling.',
        'Seek medical attention to ensure the finger heals properly and to avoid long-term deformity.'
    ],
    'Jersey Finger': [
        'Immobilize the finger and apply ice.',
        'Seek immediate medical attention, as surgery is often required to repair the injury.'
    ],
    'Boutonniere Deformity': [
        'Splint the affected finger to keep it straight.',
        'Do not bend the finger, and keep the splint on at all times unless instructed otherwise by a healthcare professional.',
        'Seek medical advice, as physical therapy or surgery may be necessary.'
    ],
    'Thumb Fracture': [
        'Immobilize the thumb with a splint or cast.',
        'Apply ice to reduce swelling and pain.',
        'Seek medical attention for proper diagnosis and treatment.'
    ],
    'Thumb Sprain': [
        'Rest the thumb and avoid movements that cause pain.',
        'Apply ice to the thumb to decrease swelling.',
        'Use a splint or brace to immobilize the thumb.',
        'Consider seeing a healthcare professional if the sprain is severe or if improvement is not seen in a few days.'
    ],
    'Skier’s Thumb': [
        'Immobilize the thumb with a splint.',
        'Apply ice to reduce swelling.',
        'Avoid using the thumb to prevent further injury.',
        'Seek medical attention, as surgery may be required for severe cases.'
    ],
    'Thumb Dislocation': [
        'Do not attempt to realign the thumb yourself.',
        'Immobilize the thumb and seek emergency medical attention for proper treatment.'
    ],
    'Arthritis (Thumb)': [
        'Apply heat to the thumb to ease stiffness.',
        'Use ice packs to reduce swelling and pain.',
        'Consider over-the-counter pain relievers or anti-inflammatory medications.',
        'Consult with a healthcare provider for specific treatments like splinting, physical therapy, or medication.'
    ],
    'Rib Fracture': [
        'Rest and avoid movements that worsen the pain.',
        'Apply ice to the affected area.',
        'Use pain relievers as prescribed by a healthcare provider.',
        'Seek medical attention, as severe fractures can damage internal organs.'
    ],
    'Sternal Fracture': [
        'Rest and limit activities to reduce pain.',
        'Apply ice to manage pain and swelling.',
        'Use over-the-counter pain medication if necessary.',
        'Seek medical care, as complications can be severe, including damage to the heart or lungs.'
    ],
    'Costochondritis': [
        'Rest and avoid activities that exacerbate the chest pain.',
        'Apply heat to the affected area to reduce pain.',
        'Consider anti-inflammatory medications to relieve discomfort.',
        'Consult a healthcare provider if pain persists or is severe.'
    ],
    'Pectoral Muscle Strain': [
        'Rest the affected muscle and avoid activities that increase pain.',
        'Apply ice to the area for the first 24-48 hours to reduce swelling.',
        'After the initial 48 hours, switch to heat to relieve pain and improve mobility.',
        'Consider taking over-the-counter anti-inflammatory medication to reduce pain and swelling.',
        'Engage in gentle stretching and strengthening exercises as recommended by a healthcare provider.'
    ],
    'Chest Contusion': [
        'Apply ice to the chest area to minimize swelling and bruising.',
        'Use over-the-counter pain relievers to manage discomfort.',
        'Wear a compression wrap if it helps to alleviate the pain, but ensure it does not restrict breathing.',
        'Monitor for difficulty breathing or coughing up blood, as these may be signs of more serious injury.'
    ],
    'Costochondral Separation': [
        'Rest and avoid movements that exacerbate the pain.',
        'Apply ice to the affected area to minimize swelling.',
        'Take over-the-counter pain medication if necessary.',
        'Consider wrapping the chest, but ensure it does not restrict breathing.'
    ],
    'Muscle Strain (Ribs)': [
        'Rest the muscle and avoid any activity that causes pain.',
        'Apply ice to the area to reduce swelling and pain.',
        'Use compression wraps to support the area if its comfortable and doesnt restrict breathing.',
        'Gentle stretching and strengthening exercises can be done after the pain subsides.'
    ],
    'Rib Contusion': [
        'Apply ice to the affected area to reduce pain and swelling.',
        'Rest and avoid activities that cause pain.',
        'Protect the area from further injury.',
        'Seek medical attention if breathing becomes difficult or if pain is severe.'
    ],
    'Pneumothorax': [
        'Seek immediate medical attention as this condition can be life-threatening.',
        'Avoid activities and rest until medical help is available.',
        'Prepare for possible hospitalization to remove air from the pleural space.'
    ],
    'Upper Back Muscle Strain': [
        'Rest the back muscles and cease any activity causing pain.',
        'Apply ice to the area initially, then heat after the acute injury has improved.',
        'Consider over-the-counter pain relievers to reduce pain and inflammation.',
        'Engage in gentle stretching and strengthening exercises as pain allows.'
    ],
    'Thoracic Spine Injury': [
        'Immobilize the area and do not move if spinal injury is suspected.',
        'Seek immediate medical attention.',
        'Use medication to control pain as recommended by a healthcare professional.',
        'Follow a rehabilitation program under the guidance of a healthcare provider.'
    ],
    'Thoracic Spine Fracture': [
        'Immobilize the spine and avoid moving.',
        'Apply ice around the injured area, not directly on the spine.',
        'Seek medical care immediately for proper assessment and treatment.'
    ],
    'Upper Back Contusion': [
        'Apply ice to the affected area to reduce swelling.',
        'Rest and protect the area from further injury.',
        'If the contusion is severe or there is difficulty breathing, seek medical attention.'
    ],
    'Thoracic Herniated Disc': [
        'Rest and avoid activities that worsen the symptoms.',
        'Apply heat or ice to the affected area based on comfort.',
        'Take medications as prescribed for pain relief.',
        'Consider physical therapy to strengthen the back muscles.'
    ],
    'Lumbar Strain': [
        'Rest the lower back and avoid heavy lifting or twisting movements.',
        'Apply ice initially, then heat to the affected area.',
        'Use over-the-counter pain relievers and muscle relaxants as needed.',
        'Gradually increase activity levels with stretching and strengthening exercises.'
    ],
    'Lumbar Herniated Disc': [
        'Rest and avoid positions and activities that cause pain.',
        'Apply ice or heat to the lower back as needed for comfort.',
        'Take nonsteroidal anti-inflammatory drugs (NSAIDs) to reduce inflammation.',
        'Consider physical therapy to improve mobility and strengthen back muscles.',
        'Surgery may be an option if conservative treatments dont relieve symptoms.'
    ],
    'Sciatica': [
        'Rest the back but do not stay immobile for too long.',
        'Apply heat or ice to the affected area for pain relief.',
        'Take over-the-counter pain relievers as needed.',
        'Perform gentle stretching exercises to reduce nerve compression.',
        'Consult a healthcare provider if the pain is severe or persistent.'
    ],
    'Spondylolisthesis': [
        'Avoid hyperextension of the back and activities that cause pain.',
        'Use a back brace if recommended by a healthcare provider.',
        'Engage in physical therapy to strengthen the abdominal and back muscles.',
        'In severe cases, surgery may be necessary to stabilize the affected vertebrae.'
    ],
    'Spinal Fracture': [
        'Do not move the person unless necessary to prevent further injury.',
        'Seek immediate medical attention.',
        'Stabilization with a brace or surgery may be required depending on the location and type of fracture.'
    ],

    'Abdominal Muscle Strain': [
        'Rest the muscle and avoid activities that may cause further strain.',
        'Apply ice to the area for the first 48 hours to reduce pain and swelling.',
        'After 48 hours, switch to heat to promote blood flow and healing.',
        'If pain persists or worsens, seek medical evaluation.'
    ],
    'Abdominal Contusion': [
        'Apply ice to the affected area to help control swelling and pain.',
        'Wear a compression wrap to provide support, if comfortable.',
        'Rest and avoid activities that cause discomfort or pain.',
        'Monitor for symptoms of internal bleeding, such as bloody urine or severe abdominal pain, and seek medical attention if these occur.'
    ],
    'Organ Injury': [
        'Seek immediate medical attention, as internal organ injuries can be life-threatening.',
        'Do not consume any food or drink if an abdominal organ injury is suspected.',
        'Prepare for diagnostic tests, such as an ultrasound, CT scan, or MRI.'
    ],
    'Abdominal Wall Tear': [
        'Rest and avoid activities that could worsen the tear.',
        'Apply ice to the area to reduce swelling and inflammation.',
        'Consider seeing a healthcare professional for evaluation and potential imaging to assess the extent of the injury.',
        'Surgery may be required to repair a significant tear.'
    ],
    'Groin Strain': [
        'Rest and avoid any activity that causes pain.',
        'Apply ice to the area to reduce pain and swelling.',
        'Use a compression short or wrap to provide support.',
        'After the acute phase, gentle stretching and strengthening exercises may be beneficial.'
    ],
    'Hernia': [
        'Avoid heavy lifting and straining.',
        'Support the area with a truss after consulting with a healthcare provider.',
        'Surgical repair may be necessary, so consult with a healthcare provider for evaluation.'
    ],
    'Testicular Contusion': [
        'Apply cold packs to the area to reduce swelling, but not directly against the skin.',
        'Wear supportive undergarments to minimize movement and discomfort.',
        'Seek medical attention if pain is severe or if there is suspicion of a more serious injury.'
    ],
    'Adductor Tendonitis': [
        'Rest the affected leg and avoid activities that worsen pain.',
        'Apply ice to the groin area to reduce inflammation and pain.',
        'Gentle stretching and strengthening exercises may be recommended by a healthcare provider.',
        'Consider physical therapy for more persistent cases.'
    ],
    'Labral Tear (Groin)': [
        'Rest and avoid movements that cause pain in the hip or groin.',
        'Apply ice to the affected area to manage pain and swelling.',
        'Physical therapy may help improve joint mobility and strength.',
        'In some cases, arthroscopic surgery may be necessary for repair.'
    ],
    'Hip Dislocation': [
        'Do not move or try to force the hip back into place.',
        'Keep the hip and leg in the position found.',
        'Seek emergency medical attention immediately.',
        'After reduction, physical therapy will be important for recovery.'
    ],
    'Hip Pointer': [
        'Apply ice to the injured area to reduce swelling and pain.',
        'Rest and avoid activities that cause pain.',
        'Use padding and protection when returning to sports activities.',
        'If pain persists, seek medical evaluation for further treatment.'
    ],
    'Hip Labral Tear': [
        'Rest the affected hip and modify activities to avoid pain.',
        'Apply ice to the hip area to reduce pain and swelling.',
        'Nonsteroidal anti-inflammatory drugs (NSAIDs) may help reduce inflammation and pain.',
        'Physical therapy may be recommended for rehabilitation.',
        'Surgical intervention may be required in cases where symptoms persist.'
    ],
    'Hip Flexor Strain': [
        'Rest the hip and avoid movements that cause pain.',
        'Apply ice to the area for the first few days to reduce pain and swelling.',
        'Gentle stretching and strengthening exercises can aid recovery once the pain begins to subside.',
        'If the strain is severe, seek medical attention for a possible physical therapy referral.'
    ],
    'Femoral Neck Fracture': [
        'Immobilize the hip and avoid putting weight on the leg.',
        'Apply ice to control pain and swelling.',
        'Seek immediate medical attention as surgery is often required.',
        'Post-surgery, engage in rehabilitation to restore hip function and strength.'
    ],
    'Quadriceps Strain': [
        'Rest and avoid activities that increase pain in the thigh.',
        'Apply ice to the affected area to reduce pain and swelling.',
        'Use a compression wrap to support the thigh muscle.',
        'Gentle stretching and strengthening exercises can be performed as the pain subsides.'
    ],
    'Hamstring Strain': [
        'Rest the leg and avoid activities that cause pain.',
        'Apply ice to the hamstring to reduce pain and swelling.',
        'Wrap the thigh to provide support if needed.',
        'Engage in gentle stretching and strengthening exercises once the acute pain is reduced.'
    ],
    'Thigh Contusion': [
        'Apply ice immediately to minimize swelling.',
        'Rest and elevate the leg to reduce bleeding into the muscle.',
        'Use a compression bandage to limit swelling and movement.',
        'If there is a significant loss of motion or function, seek medical attention.'
    ],
    'Muscle Rupture': [
        'Cease all activity and immobilize the affected muscle.',
        'Apply ice to the area and seek immediate medical attention.',
        'Surgical intervention may be required to repair the muscle.'
    ],
    'Femoral Fracture': [
        'Immobilize the leg and do not try to straighten it.',
        'Apply ice to the surrounding area to control swelling, but not directly on the fracture site.',
        'Cover any open wounds with sterile dressings.',
        'Call for emergency medical assistance immediately.'
    ],
    'Hamstring Tear': [
        'Stop any activity and apply ice to reduce pain and swelling.',
        'Elevate the leg to decrease swelling.',
        'Use a compression bandage to support the hamstring area.',
        'Rest the leg as much as possible and avoid putting weight on it.',
        'Seek medical attention to assess the need for surgery or physical therapy.'
    ],
    'Avulsion Fracture': [
        'Immobilize the affected area immediately.',
        'Apply ice to reduce swelling and pain, but ensure theres a barrier between the ice and skin.',
        'Seek medical attention promptly, as surgery may be needed to reattach the bone fragments.'
    ],
    'Hamstring Tendonitis': [
        'Rest the affected leg to prevent further irritation of the tendon.',
        'Apply ice to the hamstring to help reduce pain and inflammation.',
        'Consider taking anti-inflammatory medications if recommended by a healthcare provider.',
        'Physical therapy may be beneficial to strengthen the muscles and tendons around the hamstring.'
    ],
    'ACL Injury': [
        'Immediately stop activity and apply ice to reduce swelling.',
        'Use a compression bandage and elevate the knee above heart level.',
        'Seek medical attention for a proper diagnosis and potential surgery.',
        'Follow a rehabilitation program post-surgery or as part of conservative treatment.'
    ],
    'MCL Injury': [
        'Apply ice to the knee and rest.',
        'Use a brace or bandage to immobilize the knee if necessary.',
        'Avoid activities that put stress on the knee until fully healed.',
        'Consider physical therapy to strengthen the surrounding muscles.'
    ],
    'Meniscus Tear': [
        'Rest the knee and apply ice to reduce pain and swelling.',
        'Elevate the leg and use a compression wrap.',
        'Seek medical evaluation, as some tears may require surgery.',
        'Engage in rehabilitation exercises to restore range of motion.'
    ],
    'Patellar Fracture': [
        'Immobilize the knee and avoid putting weight on it.',
        'Apply ice to control swelling and alleviate pain.',
        'Seek medical attention for potential surgery or immobilization with a cast.',
        'Participate in physical therapy for recovery after immobilization or surgery.'
    ],
    'Knee Tendonitis': [
        'Rest the knee and avoid activities that worsen the pain.',
        'Apply ice to the affected area to reduce inflammation and pain.',
        'Use a knee support or strap as directed by a healthcare provider.',
        'Perform stretching and strengthening exercises recommended by a professional.'
    ],
    'Shin Splints': [
        'Rest from activities that cause shin pain.',
        'Apply ice to the shins for 20-30 minutes every 3 to 4 hours to reduce pain and swelling.',
        'Wear proper footwear with adequate cushioning and support.',
        'Consider physical therapy to strengthen the muscles around the shin.'
    ],
    'Stress Fracture (Shin)': [
        'Rest and avoid weight-bearing activities.',
        'Apply ice to the affected area to reduce swelling and pain.',
        'Seek medical attention for proper diagnosis and management.',
        'Gradually return to activity once healed, with proper footwear and possibly orthotics.'
    ],
    'Deep Vein Thrombosis (Shin)': [
        'Do not massage or apply heat to the area, which could dislodge a clot.',
        'Seek immediate medical attention as this condition can be life-threatening.',
        'Medication to thin the blood may be prescribed to prevent clot growth and reduce the risk of embolism.'
    ],
    'Shin Contusion': [
        'Apply ice to the shin to reduce pain and swelling.',
        'Rest and elevate the leg.',
        'Protect the area from further impact.',
        'Seek medical attention if pain and swelling persist or if there are concerns about a fracture.'
    ],
    'Calf Strain': [
        'Rest the calf muscle and avoid activities that cause pain.',
        'Apply ice wrapped in a towel to the affected area.',
        'Use a compression bandage to support the calf.',
        'Elevate the leg to reduce swelling.'
    ],
    'Calf Tear': [
        'Immediately cease any activity and rest the leg.',
        'Apply ice to the calf for the first 24-48 hours.',
        'Compress the calf with a bandage and keep the leg elevated.',
        'Seek medical attention to determine the severity of the tear.'
    ],
    'Baker’s Cyst': [
        'Rest and avoid activities that cause knee pain.',
        'Apply ice and elevate the leg to reduce swelling.',
        'Use over-the-counter pain relievers if needed.',
        'Consult with a healthcare provider for further treatment, which may include draining the cyst or physical therapy.'
    ],
    'Calf Compartment Syndrome': [
        'Recognize this as a potential medical emergency and seek immediate medical care.',
        'Do not engage in physical activity or apply ice or compression.',
        'Surgical intervention may be required to relieve the pressure.'
    ],
    'Calf Deep Vein Thrombosis': [
        'Seek medical care immediately as this is a serious condition.',
        'Do not massage or compress the area.',
        'Follow medical advice, which may include medication to prevent clotting and monitoring.'
    ],
    'Ankle Sprain': [
        'Rest, ice, compress, and elevate the ankle (RICE method).',
        'Use a brace or bandage to stabilize the ankle.',
        'Avoid putting weight on the ankle until it starts to heal.',
        'Gradually increase movement as the pain allows to promote flexibility and strength.',
        'If the sprain is severe or doesnt improve, seek medical attention.'
    ],
    'Ankle Fracture': [
        'Immobilize the ankle and avoid bearing weight on it.',
        'Apply ice to reduce swelling and pain.',
        'Seek medical attention for a proper diagnosis and treatment plan, which may include casting or surgery.',
        'Follow a rehabilitation program after immobilization to regain strength and mobility.'
    ],
    'Achilles Tendonitis': [
        'Rest the affected ankle to reduce stress on the tendon.',
        'Apply ice to the area to decrease inflammation and pain.',
        'Elevate the foot to reduce swelling.',
        'Engage in stretching and strengthening exercises as recommended by a healthcare provider.',
        'Consider wearing a heel lift to reduce strain on the Achilles tendon.'
    ],
    'Ankle Impingement': [
        'Rest the ankle and avoid activities that exacerbate pain.',
        'Apply ice to reduce inflammation and swelling.',
        'Use anti-inflammatory medications as recommended by a healthcare provider.',
        'Physical therapy may be beneficial to improve range of motion and strength.'
    ],
    'Pott’s Fracture': [
        'Immobilize the ankle and refrain from putting weight on it.',
        'Apply ice and keep the ankle elevated to manage swelling.',
        'Seek immediate medical care, as this type of fracture usually requires a cast or surgical intervention.',
        'Follow up with physical therapy to restore ankle function.'
    ],
    'Plantar Fasciitis': [
        'Rest the foot and avoid activities that cause heel pain.',
        'Apply ice to the heel to reduce pain and inflammation.',
        'Perform stretching exercises for the Achilles tendon and plantar fascia.',
        'Use shoe inserts or orthotic devices to support the arch of the foot.',
        'Seek medical advice if pain persists, as physical therapy or other treatments may be necessary.'
    ],
    'Heel Spur': [
        'Rest and apply ice to the affected area to reduce inflammation.',
        'Engage in stretching exercises to relieve tension in the plantar fascia.',
        'Wear appropriate footwear with cushioned heels and good arch support.',
        'Consider over-the-counter pain relievers or corticosteroid injections as advised by a healthcare provider.'
    ],
    'Achilles Tendonitis': [
        'Rest the foot and reduce activities that stress the Achilles tendon.',
        'Apply ice to the affected area after activity to reduce pain and swelling.',
        'Elevate the foot to decrease swelling.',
        'Perform gentle stretching exercises for the calf muscles.',
        'Seek medical attention if pain increases or if there is no improvement with home treatment.'
    ],
    'Bursitis (Heel)': [
        'Rest the foot and avoid putting pressure on the heel.',
        'Apply ice to the heel to control pain and reduce swelling.',
        'Use over-the-counter anti-inflammatory medication to relieve pain.',
        'Consider using heel pads or cushions in shoes to reduce stress on the heel.',
        'If symptoms persist, consult a healthcare provider for additional treatment options.'
    ],
    'Heel Stress Fracture': [
        'Rest and avoid weight-bearing activities to allow the bone to heal.',
        'Apply ice to the affected area and use padding to cushion the heel.',
        'Use a brace or boot to immobilize the foot if recommended by a healthcare provider.',
        'Gradually resume activity under the guidance of a healthcare professional to prevent re-injury.'
    ],
    'Foot Fracture': [
        'Stop any activity and immobilize the foot.',
        'Apply ice and elevate the foot to reduce swelling.',
        'Use crutches or a brace as needed to keep weight off the injured foot.',
        'Seek medical attention to obtain proper treatment, which may include casting or surgery.'
    ],
    'Foot Sprain': [
        'Follow the RICE protocol: Rest, Ice, Compression, and Elevation.',
        'Use a brace or supportive shoes to protect the foot.',
        'Avoid activities that cause pain or stress on the foot.',
        'If the sprain is severe, or if symptoms persist, consult a healthcare provider.'
    ],
    'Metatarsalgia': [
        'Rest the foot and apply ice to the affected area.',
        'Use metatarsal pads in shoes to relieve pressure on the ball of the foot.',
        'Take over-the-counter pain relievers to manage discomfort.',
        'Engage in foot exercises to strengthen the muscles and improve flexibility.'
    ],
    'Toe Fracture': [
        'Immobilize the toe by buddy taping it to an adjacent toe.',
        'Apply ice and elevate the foot to reduce pain and swelling.',
        'Wear stiff-soled shoes to protect the toe and limit movement.',
        'If the fracture is severe, misaligned, or involves the big toe, seek medical attention.'
    ],
    'Toe Dislocation': [
        'Do not attempt to realign the toe yourself.',
        'Immobilize the toe and seek medical attention for proper reduction.',
        'Apply ice to reduce pain and swelling.',
        'Rest the toe and avoid putting weight on it until it heals.'
    ],
    'Gout': [
        'Rest the affected joint and keep it elevated.',
        'Apply ice to reduce inflammation and pain.',
        'Drink plenty of fluids to stay hydrated and help flush out uric acid.',
        'Avoid foods high in purines, which can trigger gout attacks.',
        'Seek medical attention for medications that can help reduce uric acid levels and pain.'
    ],
    'Ingrown Toenail': [
        'Soak the foot in warm water several times a day to reduce pain and swelling.',
        'Gently lift the edge of the ingrown nail and place a small piece of cotton underneath to separate the nail from the skin.',
        'Wear comfortable shoes with ample room for the toes.',
        'If infection or severe pain occurs, seek medical attention for possible removal of part of the nail.'
    ],
    'Toe Bunion': [
        'Wear wide, comfortable shoes with a soft sole to relieve pressure.',
        'Apply ice packs to reduce swelling.',
        'Use non-medicated bunion pads to cushion the painful area.',
        'Consider over-the-counter pain relievers to manage discomfort.',
        'Consult with a healthcare provider for persistent pain, which may require surgery or other interventions.'
    ]
  }

# Function to simulate the user interaction for injury selection and treatment recommendations
def get_treatment_recommendations():
    # Ask the user for the body part where the injury is located
    print("Please select the body part where the injury is located:")
    for part in body_parts:
        print(part)
    body_part = input("Enter the body part: ")

    # Validate the body part
    if body_part not in body_parts:
        print("Invalid body part entered. Please try again.")
        return

    # List the 5 most common injuries for that body part
    injuries = common_injuries.get(body_part, ["No common injuries listed for this body part."])
    print("\nSelect your injury from the list of common injuries for the " + body_part + ":")
    for idx, injury in enumerate(injuries, 1):
        print(f"{idx}. {injury}")
    print(f"{len(injuries) + 1}. Not sure")

    injury_index = input("Enter the number of your injury: ")

    # Validate the selected injury
    try:
        injury_index = int(injury_index) - 1
        if injury_index not in range(len(injuries)):
            if injury_index == len(injuries):
                not_sure_flow()
                return
            else:
                raise ValueError
        selected_injury = injuries[injury_index]
    except ValueError:
        print("Invalid selection. Please enter a number from the list.")
        return

    # Provide treatment steps
    treatment_steps = injury_treatment.get(selected_injury, ["No treatment recommendation available for this injury."])
    print("\nFollow these steps to treat your injury:")
    for step in treatment_steps:
        print(step)


# Call the function to start the program
get_treatment_recommendations()

