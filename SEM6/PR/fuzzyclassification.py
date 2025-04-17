import cv2
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

# Define fuzzy variables
brightness = ctrl.Antecedent(np.arange(0, 256, 1), 'brightness')
edge_intensity = ctrl.Antecedent(np.arange(0, 256, 1), 'edge_intensity')
classification = ctrl.Consequent(np.arange(0, 101, 1), 'classification')

# Membership functions for brightness
brightness['dark'] = fuzz.trimf(brightness.universe, [0, 50, 100])
brightness['normal'] = fuzz.trimf(brightness.universe, [50, 127, 200])
brightness['bright'] = fuzz.trimf(brightness.universe, [150, 200, 255])

# Membership functions for edge intensity
edge_intensity['low'] = fuzz.trimf(edge_intensity.universe, [0, 50, 100])
edge_intensity['medium'] = fuzz.trimf(edge_intensity.universe, [50, 127, 200])
edge_intensity['high'] = fuzz.trimf(edge_intensity.universe, [150, 200, 255])

# Membership functions for classification
classification['low'] = fuzz.trimf(classification.universe, [0, 25, 50])
classification['medium'] = fuzz.trimf(classification.universe, [25, 50, 75])
classification['high'] = fuzz.trimf(classification.universe, [50, 75, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(brightness['dark'] | edge_intensity['low'], classification['low'])
rule2 = ctrl.Rule(brightness['normal'] | edge_intensity['medium'], classification['medium'])
rule3 = ctrl.Rule(brightness['bright'] | edge_intensity['high'], classification['high'])

# Create control system
classification_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
classifier = ctrl.ControlSystemSimulation(classification_ctrl)

def real_time_image_classification():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness_value = np.mean(gray)
        
        edges = cv2.Canny(gray, 100, 200)
        edge_intensity_value = np.mean(edges)
        
        classifier.input['brightness'] = brightness_value
        classifier.input['edge_intensity'] = edge_intensity_value
        classifier.compute()
        classification_result = classifier.output['classification']
        
        cv2.putText(frame, f'Classification: {classification_result:.2f}', (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('Real-Time Classification', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    real_time_image_classification()
