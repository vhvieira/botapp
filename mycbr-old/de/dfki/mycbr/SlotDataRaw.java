/*
 * myCBR License 1.1
 *
 * Copyright (c) 2008
 * Thomas Roth-Berghofer, Armin Stahl & Deutsches Forschungszentrum f&uuml;r K&uuml;nstliche Intelligenz DFKI GmbH
 * Further contributors: myCBR Team (see http://mycbr-project.net/contact.html for further information 
 * about the myCBR Team). 
 * All rights reserved.
 *
 * myCBR is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 * Since myCBR uses some modules, you should be aware of their licenses for
 * which you should have received a copy along with this program, too.
 * 
 * endOfLic */
package de.dfki.mycbr;

import java.io.Serializable;
import java.util.Collection;

/**
 * Slots created using XML files first are SlotDataRawImpl objects.
 * Then they are passed to ClsDataRaw objects which then can be used by the modelprovider to build CaseInstance objects
 * 
 * @author myCBR Team
 */
public interface SlotDataRaw extends Serializable {
	
	/**
	 * Getter for the name of this slot
	 * @return the name of this slot
	 */
	public String getName();
	
	/**
	 * Getter for the value type of this slot 
	 * @return the value type of this slot
	 * @see ValueType
	 */
	public ValueType getValueType();
	
	/**
	 * Getter for the allowed values of this slot.
	 * Used for slots havin SYMBOL as value type.
	 * @return a collection of the allowd values of this slot
	 */
	public Collection<String> getAllowedValues();
	
	/**
	 * Getter for the minimum value of this slot.
	 * Used for slots having INTEGER or FLOAT as value type. 
	 * @return the minimum value of this slot
	 */
	public Number getMinimumValue();

	/**
	 * Getter for the maximum value of this slot.
	 * Used for slots having INTEGER or FLOAT as value type. 
	 * @return the maximum value of this slot
	 */
	public Number getMaximumValue();

	/**
	 * A slot can be multiple, meaning that you are allowed to specify
	 * more than one value (of the slots value type) for this slot.
	 * @return true, if this slot is multiple. false, otherwise.
	 */
	public boolean isMultiple();

}
