def load_model():
   from transformers import AutoModelForCausalLM, AutoTokenizer
   model_id = "some-org/some-model"
   # Risky supply-chain behavior
   tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
   mdl = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
   return mdl, tok
