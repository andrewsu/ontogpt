from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union, Literal
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal

metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'
    
class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True, 
                validate_all = True, 
                underscore_attrs_are_private = True, 
                extra = 'forbid', 
                arbitrary_types_allowed = True):
    pass                    


class NullDataOptions(str, Enum):
    
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"
    
    

class GenemiRNARelationship(ConfiguredBaseModel):
    
    gene: Optional[str] = Field(None)
    miRNA: Optional[str] = Field(None)
    


class GeneDiseaseRelationship(ConfiguredBaseModel):
    
    gene: Optional[str] = Field(None)
    disease: Optional[str] = Field(None)
    


class MiRNADiseaseRelationship(ConfiguredBaseModel):
    
    gene: Optional[str] = Field(None)
    disease: Optional[str] = Field(None)
    


class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""")
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""")
    


class NamedEntity(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    


class MiRNA(NamedEntity):
    
    label: Optional[str] = Field(None, description="""the name of the miRNA""")
    description: Optional[str] = Field(None, description="""a textual description of the miRNA""")
    synonyms: Optional[List[str]] = Field(default_factory=list, description="""alternative names of the miRNA""")
    disease: Optional[List[str]] = Field(default_factory=list)
    miRNA_disease: Optional[List[MiRNADiseaseRelationship]] = Field(default_factory=list, description="""semicolon-separated list of miRNA to disease relationships""")
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    


class Gene(NamedEntity):
    
    label: Optional[str] = Field(None, description="""the name of the gene""")
    description: Optional[str] = Field(None, description="""a textual description of the gene""")
    synonyms: Optional[List[str]] = Field(default_factory=list, description="""alternative names of the gene""")
    miRNAs: Optional[List[str]] = Field(default_factory=list)
    disease: Optional[List[str]] = Field(default_factory=list)
    gene_miRNA: Optional[List[GenemiRNARelationship]] = Field(default_factory=list, description="""semicolon-separated list of gene to miRNA relationships""")
    gene_disease: Optional[List[GeneDiseaseRelationship]] = Field(default_factory=list, description="""semicolon-separated list of gene to disease relationships""")
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    


class Disease(NamedEntity):
    
    label: Optional[str] = Field(None, description="""the name of the disease""")
    description: Optional[str] = Field(None, description="""a textual description of the disease""")
    synonyms: Optional[List[str]] = Field(default_factory=list, description="""alternative names of the disease""")
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    


class CompoundExpression(ConfiguredBaseModel):
    
    None
    


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    


class TextWithTriples(ConfiguredBaseModel):
    
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)
    


class RelationshipType(NamedEntity):
    
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    


class Publication(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    combined_text: Optional[str] = Field(None)
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")
    


class AnnotatorResult(ConfiguredBaseModel):
    
    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
GenemiRNARelationship.update_forward_refs()
GeneDiseaseRelationship.update_forward_refs()
MiRNADiseaseRelationship.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
MiRNA.update_forward_refs()
Gene.update_forward_refs()
Disease.update_forward_refs()
CompoundExpression.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
