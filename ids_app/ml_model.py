from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle
import os

class IDSModel:
    def __init__(self):
        self.model = None
        self.model_path = os.path.join(os.path.dirname(__file__), 'models', 'ids_model.pkl')
        self.load_model()
    
    def load_model(self):
        try:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
        except:
            # Initialize a new model if none exists
            self.model = RandomForestClassifier(n_estimators=100)
    
    def predict(self, features):
        """
        Predict if a log entry is malicious
        features: numpy array of features extracted from log
        returns: probability of being malicious
        """
        if self.model is None:
            return 0.5  # Default if no model
        
        return self.model.predict_proba(features.reshape(1, -1))[0][1]
    
    def train(self, X, y):
        """
        Train the model on new data
        X: features
        y: labels (0 for normal, 1 for intrusion)
        """
        self.model.fit(X, y)
        
        # Save the model
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f) 