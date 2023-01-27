const Joi = require('joi');

const { createCategorySchema } = require('./category.schema');

const id = Joi.string().guid({ version: 'uuidv4' });
const name = Joi.string().min(3).max(15).alphanum();
const price = Joi.number().integer().min(10);
const description = Joi.string().min(8).max(15);
const image = Joi.string().uri();

const createProductSchema = Joi.object({
  name: name.required(),
  price: price.required(),
  description: description.required(),
  image: image.required(),
  categoryId: createCategorySchema.id.required(),
});

const updateProductSchema = Joi.object({
  name: name,
  price: price,
  description: description,
  image: image,
  categoryId: createCategorySchema.id,
});

const productIdSchema = Joi.object({
  id: id.required(),
});

module.exports = {
  productIdSchema,
  createProductSchema,
  updateProductSchema,
};
