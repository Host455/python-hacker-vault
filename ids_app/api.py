from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Analysis
from .serializers import AnalysisSerializer

class AnalysisViewSet(viewsets.ModelViewSet):
    """API endpoint for analysis results"""
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Analysis.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    def analyze_log(self, request):
        """API endpoint to submit a log for analysis"""
        log_file = request.FILES.get('logfile')
        if not log_file:
            return Response({'error': 'No log file provided'}, status=400)
            
        # Process the log file
        # ...
        
        return Response({'status': 'success', 'message': 'Analysis complete'}) 