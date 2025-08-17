import logging
from pathlib import Path
from typing import List, Protocol, Optional
from pypdf import PdfReader


class DocumentLoader(Protocol):
    """Protocol for document loading implementations."""
    
    def load_document(self, file_path: str) -> List[str]:
        """Load document content from file path."""
        ...


class PDFLoader:
    """PDF document loader implementation."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
    
    def load_document(self, file_path: str) -> List[str]:
        """
        Load data from a PDF file.

        Args:
            file_path (str): The path to the PDF file.

        Returns:
            List[str]: A list of text content extracted from each page.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            Exception: If PDF reading fails.
        """
        path = Path(file_path)
        
        if not path.exists():
            self.logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if not path.suffix.lower() == '.pdf':
            self.logger.error(f"File is not a PDF: {file_path}")
            raise ValueError(f"Expected PDF file, got: {path.suffix}")
            
        try:
            pdf_reader = PdfReader(str(path))
            text_content = []
            
            for page_num, page in enumerate(pdf_reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text.strip():  # Only add non-empty pages
                        text_content.append(page_text)
                    else:
                        self.logger.warning(f"Empty content on page {page_num + 1} of {file_path}")
                except Exception as e:
                    self.logger.warning(f"Failed to extract text from page {page_num + 1} of {file_path}: {e}")
                    
            if not text_content:
                self.logger.warning(f"No text content extracted from {file_path}")
                
            return text_content
            
        except Exception as e:
            self.logger.error(f"Failed to read PDF {file_path}: {e}")
            raise


class DataLoaderService:
    """Service for loading documents using various loaders."""
    
    def __init__(self, pdf_loader: Optional[DocumentLoader] = None):
        self.pdf_loader = pdf_loader or PDFLoader()
        self.logger = logging.getLogger(__name__)
    
    def load_data_from(self, file_path: str) -> List[str]:
        """
        Load data from a file based on its extension.
        
        Args:
            file_path (str): Path to the file to load.
            
        Returns:
            List[str]: Extracted text content.
        """
        path = Path(file_path)
        
        if path.suffix.lower() == '.pdf':
            return self.pdf_loader.load_document(file_path)
        else:
            self.logger.error(f"Unsupported file type: {path.suffix}")
            raise ValueError(f"Unsupported file type: {path.suffix}")